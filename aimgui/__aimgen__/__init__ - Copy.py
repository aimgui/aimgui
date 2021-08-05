import os
import re
import sys
import collections
import pathlib
import toml

from clang import cindex

from aimgen import UserSet

HEADER = """
#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <limits>
#include "imgui.h"
#include "imgui_internal.h"

#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_generated(py::module &libaimgui, Registry &registry) {
"""

FOOTER = """
}
"""

DEFAULTS = {
    'out_h' : '0',
    'out_s' : '0',
    'out_v' : '0',
    'out_r' : '0',
    'out_g' : '0',
    'out_g' : '0',
    'out_ini_size' : '0',
}

def snakecase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Options:
    def __init__(self, *options, **kwargs):
        for dictionary in options:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class Overloaded(UserSet):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.visited = set()

    def is_overloaded(self, cursor):
        return self.name(cursor) in self

class Out:
    def __init__(self) -> None:
        self.file = None
        self.indent = 0

    def __call__(self, line):
        if len(line):
            self.file.write(' ' * self.indent * 4)
            self.file.write(line.replace('>>', '> >'))
        self.file.write('\n')

class Generator:
    def __init__(self, *config, **kwargs):
        self.out = Out()
        #
        self.options = { 'save': True }
        for dictionary in config:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            if key == 'options':
                options = kwargs[key]
                options.update(self.options)
                self.options = options

            setattr(self, key, kwargs[key])

        
        self.options = Options(self.options)
        self.overloaded = Overloaded(self.overloaded)

    @classmethod
    def create(self, filename="aimgen.toml"):
        config = toml.load(filename)
        instance = Generator(config)
        return instance

    def format_attribute(self, name):
        name = snakecase(name)
        name = name.rstrip('_')
        name = name.replace('__', '_')
        return name

    def format_type(self, name):
        name = name.replace('ImGui', '')
        name = name.replace('Im', '')
        name = name.replace('<', '_')
        name = name.replace('>', '')
        name = name.replace(' ', '')
        name = name.rstrip('_')
        return name

    def format_enum(self, name):
        name = name.replace('ImGui', '')
        name = name.replace('Im', '')
        name = snakecase(name).upper()
        name = name.replace('__', '_')
        name = name.rstrip('_')
        return name

    def module(self, cursor):
        if cursor is None:
            return 'libaimgui'
        else:
            return self.format_type(cursor.spelling)

    def is_excluded(self, cursor):
        if self.name(cursor) in self.excludes:
            return True
        if cursor.spelling.startswith('_'):
            return True
        return False

    def name(self, cursor):
        if cursor is None:
            return ''
        elif cursor.kind == cindex.CursorKind.TRANSLATION_UNIT:
            return ''
        else:
            res = self.name(cursor.semantic_parent)
            if res != '':
                return res + '::' + cursor.spelling
        return cursor.spelling

    def is_class_mappable(self, cursor):
        if not cursor.is_definition():
            return False
        if self.is_excluded(cursor):
            return False
        return True

    def is_function_mappable(self, cursor):
        if 'operator' in cursor.spelling:
            return False
        if self.is_excluded(cursor):
            return False
        for argument in cursor.get_arguments():
            if argument.type.get_canonical().kind == cindex.TypeKind.POINTER:
                ptr = argument.type.get_canonical().get_pointee().kind
                if ptr == cindex.TypeKind.FUNCTIONPROTO:
                    return False
            if argument.type.spelling == 'va_list':
                return False
        return True

    def is_function_void_return(self, cursor):
        result = cursor.type.get_result()
        return result.kind == cindex.TypeKind.VOID

    def is_property_mappable(self, cursor):
        if self.is_excluded(cursor):
            return False
        return True

    def is_cursor_mappable(self, cursor):
        if cursor.location.file:
            return 'imgui.h' in cursor.location.file.name
        return False

    def is_property_readonly(self, cursor):
        if cursor.type.kind == cindex.TypeKind.CONSTANTARRAY:
            return True
        return False

    def is_overloaded(self, cursor):
        return self.name(cursor) in self.overloaded

    def arg_type(self, argument):
        if argument.type.kind == cindex.TypeKind.CONSTANTARRAY:
            return f'std::array<{argument.type.get_array_element_type().spelling}, {argument.type.get_array_size()}>&'
        return argument.type.spelling

    def arg_name(self, argument):
        if argument.type.kind == cindex.TypeKind.CONSTANTARRAY:
            return f'&{argument.spelling}[0]'
        return argument.spelling

    def arg_types(self, arguments):
        return ', '.join([self.arg_type(a) for a in arguments])

    def arg_names(self, arguments):
        return ', '.join([self.arg_name(a) for a in arguments])

    def arg_string(self, arguments):
        return ', '.join(['{} {}'.format(self.arg_type(a), a.spelling) for a in arguments])

    def default_from_tokens(self, tokens):
        joined = ''.join([t.spelling for t in tokens])
        parts = joined.split('=')
        if len(parts) == 2:
            return parts[1]
        return ''

    def write_pyargs(self, arguments):
        for argument in arguments:
            default = self.default_from_tokens(argument.get_tokens())
            for child in argument.get_children():
                if child.type.kind in [cindex.TypeKind.POINTER]:
                    default = 'nullptr'
                elif not len(default):
                    default = self.default_from_tokens(child.get_tokens())
            default = DEFAULTS.get(argument.spelling, default)
            if len(default):
                default = ' = ' + default
            self.out(f', py::arg("{self.format_attribute(argument.spelling)}"){default}')

    def parse_enum(self, cursor):
        self.out(f'py::enum_<{self.name(cursor)}>(libaimgui, "{self.format_type(cursor.spelling)}", py::arithmetic())')
        self.out.indent += 1
        for value in cursor.get_children():
            self.out(f'.value("{self.format_enum(value.spelling)}", {value.spelling})')
        self.out('.export_values();')
        self.out.indent -= 1
        self.out('')

    def parse_constructor(self, cursor, cls):
        arguments = [a for a in cursor.get_arguments()]
        if len(arguments):
            self.out(f'{self.module(cls)}.def(py::init<{self.arg_types(arguments)}>()')
            self.write_pyargs(arguments)
            self.out(');')
        else:
            self.out(f'{self.module(cls)}.def(py::init<>());')

    def parse_field(self, cursor, cls):
        pyname = self.format_attribute(cursor.spelling)
        cname = self.name(cursor)
        if self.is_property_mappable(cursor):
            if self.is_property_readonly(cursor):
                self.out(f'{self.module(cls)}.def_readonly("{pyname}", &{cname});')
            else:
                self.out(f'{self.module(cls)}.def_readwrite("{pyname}", &{cname});')

    def should_wrap_function(self, cursor):
        if cursor.type.is_function_variadic():
            return True
        for arg in cursor.get_arguments():
            if arg.type.kind == cindex.TypeKind.CONSTANTARRAY:
                return True
            if self.should_return_argument(arg):
                return True
        return False

    def should_return_argument(self, argument):
        argtype = argument.type.get_canonical()
        if argtype.kind == cindex.TypeKind.LVALUEREFERENCE:
            if not argtype.get_pointee().is_const_qualified():
                return True
        if argtype.kind == cindex.TypeKind.CONSTANTARRAY:
            return True
        if argtype.kind == cindex.TypeKind.POINTER:
            ptr = argtype.get_pointee()
            kinds = [
                cindex.TypeKind.BOOL,
                cindex.TypeKind.FLOAT,
                cindex.TypeKind.DOUBLE,
                cindex.TypeKind.INT,
                cindex.TypeKind.UINT,
                cindex.TypeKind.USHORT,
                cindex.TypeKind.ULONG,
                cindex.TypeKind.ULONGLONG,
            ]
            if not ptr.is_const_qualified() and ptr.kind in kinds:
                return True
        return False

    def get_function_return(self, cursor):
        returned = [a.spelling for a in cursor.get_arguments() if self.should_return_argument(a)]
        if not self.is_function_void_return(cursor):
            returned.insert(0, 'ret')
        if len(returned) > 1:
            return 'std::make_tuple({})'.format(', '.join(returned))
        if len(returned) == 1:
            return returned[0]
        return ''

    def get_return_policy(self, cursor):
        result = cursor.type.get_result()
        if result.kind == cindex.TypeKind.LVALUEREFERENCE:
            return 'py::return_value_policy::reference'
        else:
            return 'py::return_value_policy::automatic_reference'

    def parse_function(self, cursor, cls=None):
        if self.is_function_mappable(cursor):
            mname = self.module(cls)
            arguments = [a for a in cursor.get_arguments()]
            cname = '&' + self.name(cursor)
            pyname = self.format_attribute(cursor.spelling)
            if self.is_overloaded(cursor):
                cname = f'py::overload_cast<{self.arg_types(arguments)}>({cname})'
            if self.should_wrap_function(cursor):
                self.out(f'{mname}.def("{pyname}", []({self.arg_string(arguments)})')
                self.out('{')
                ret = '' if self.is_function_void_return(cursor) else 'auto ret = '
                self.out(f'    {ret}{self.name(cursor)}({self.arg_names(arguments)});')
                self.out(f'    return {self.get_function_return(cursor)};')
                self.out('}')
            else:
                self.out(f'{mname}.def("{pyname}", {cname}')
            self.write_pyargs(arguments)
            self.out(f', {self.get_return_policy(cursor)});')

    def parse_class(self, cursor):
        if self.is_class_mappable(cursor):
            clsname = self.name(cursor)
            pyname = self.format_type(cursor.spelling)
            #TODO:this is a total hack.  Is it because it's private or something?
            if clsname == '':
                return
                #print('Unnamed class!', cursor.__dict__)
                #pyname = "ImContext"
                #clsname = "ImGuiContext"
            self.out(f'PYCLASS_BEGIN(libaimgui, {clsname}, {pyname})')
            for child in cursor.get_children():
                if child.kind == cindex.CursorKind.CONSTRUCTOR:
                    self.parse_constructor(child, cursor)
                elif child.kind == cindex.CursorKind.CXX_METHOD:
                    self.parse_function(child, cursor)
                elif child.kind == cindex.CursorKind.FIELD_DECL:
                    self.parse_field(child, cursor)
            self.out(f'PYCLASS_END(libaimgui, {clsname}, {pyname})\n')

    def parse_definitions(self, root):
        for cursor in root.get_children():
            if cursor.kind == cindex.CursorKind.ENUM_DECL:
                self.parse_enum(cursor)
            elif cursor.kind == cindex.CursorKind.STRUCT_DECL:
                self.parse_class(cursor)
            elif cursor.kind == cindex.CursorKind.FUNCTION_DECL:
                self.parse_function(cursor)
            elif cursor.kind == cindex.CursorKind.NAMESPACE:
                self.parse_definitions(cursor)

    def parse_overloads(self, cursor):
        for child in cursor.get_children():
            if child.kind in [cindex.CursorKind.CXX_METHOD, cindex.CursorKind.FUNCTION_DECL]:
                key = self.name(child)
                if key in self.overloaded.visited:
                    self.overloaded.add(key)
                else:
                    self.overloaded.visited.add(key)
            elif self.is_cursor_mappable(child):
                self.parse_overloads(child)

    def generate(self):
        if sys.platform == 'darwin':
            cindex.Config.set_library_path('/usr/local/opt/llvm@6/lib')
        elif sys.platform == 'win32':
            #cindex.Config.set_library_file('libclang.dll')
            cindex.Config.set_library_path('C:/Program Files/LLVM/bin')
        else:
            cindex.Config.set_library_file('libclang-10.so')

        BASE_PATH = pathlib.Path('.')
        path = BASE_PATH / self.source
        tu = cindex.Index.create().parse(path, args=self.flags)
        self.out.file = open(BASE_PATH / self.target, 'w')
        self.out.indent = 0
        self.out(HEADER)
        self.out.indent = 1
        self.parse_overloads(tu.cursor)
        self.parse_definitions(tu.cursor)
        self.out.indent = 0
        self.out(FOOTER)
