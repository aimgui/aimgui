import os
import re
import sys
import collections
import pathlib
import toml

from clang import cindex

from . import UserSet

from abc import ABC, abstractmethod

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

    def is_overloaded(self, node):
        return self.name(node) in self

class Out:
    def __init__(self) -> None:
        self.file = None
        self.indent = 0

    def __call__(self, line):
        if len(line):
            self.file.write(' ' * self.indent * 4)
            self.file.write(line.replace('>>', '> >'))
        self.file.write('\n')

class GeneratorABC(ABC):
    def __init__(self, *config, **kwargs):
        self.out = Out()
        #
        # Injected members
        # TODO: Validate after injection
        #
        self.source = None
        self.mapped = None
        self.target = None
        self.prefix = None
        self.short_prefix = None
        self.module = None
        self.flags = None
        self.excludes = None
        self.overloaded = None
        # End Injected members

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

    @property
    @abstractmethod
    def header(self):
        pass

    @property
    @abstractmethod
    def footer(self):
        pass

    @property
    @abstractmethod
    def defaults(self):
        pass

    def format_attribute(self, name):
        name = snakecase(name)
        name = name.rstrip('_')
        name = name.replace('__', '_')
        return name

    def format_type(self, name):
        name = name.replace(self.prefix, '')
        name = name.replace(self.short_prefix, '')
        name = name.replace('<', '_')
        name = name.replace('>', '')
        name = name.replace(' ', '')
        name = name.rstrip('_')
        return name

    def format_enum(self, name):
        name = name.replace(self.prefix, '')
        name = name.replace(self.short_prefix, '')
        name = snakecase(name).upper()
        name = name.replace('__', '_')
        name = name.rstrip('_')
        return name

    def module_(self, node):
        if node is None:
            return self.module
        else:
            return self.format_type(node.spelling)

    def is_excluded(self, node):
        if self.name(node) in self.excludes:
            return True
        if node.spelling.startswith('_'):
            return True
        return False

    def name(self, node):
        if node is None:
            return ''
        elif node.kind == cindex.CursorKind.TRANSLATION_UNIT:
            return ''
        else:
            res = self.name(node.semantic_parent)
            if res != '':
                return res + '::' + node.spelling
        return node.spelling

    def is_class_mappable(self, node):
        if not node.is_definition():
            return False
        if self.is_excluded(node):
            return False
        return True

    def is_function_mappable(self, node):
        if 'operator' in node.spelling:
            return False
        if self.is_excluded(node):
            return False
        for argument in node.get_arguments():
            if argument.type.get_canonical().kind == cindex.TypeKind.POINTER:
                ptr = argument.type.get_canonical().get_pointee().kind
                if ptr == cindex.TypeKind.FUNCTIONPROTO:
                    return False
            if argument.type.spelling == 'va_list':
                return False
        return True

    def is_function_void_return(self, node):
        result = node.type.get_result()
        return result.kind == cindex.TypeKind.VOID

    def is_property_mappable(self, node):
        if self.is_excluded(node):
            return False
        return True

    def is_node_mappable(self, node):
        if node.location.file:
            return self.mapped in node.location.file.name
        return False

    def is_property_readonly(self, node):
        if node.type.kind == cindex.TypeKind.CONSTANTARRAY:
            return True
        return False

    def is_overloaded(self, node):
        return self.name(node) in self.overloaded

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
            default = self.defaults.get(argument.spelling, default)
            #print(argument.spelling)
            #print(default)
            if len(default):
                default = ' = ' + default
            self.out(f', py::arg("{self.format_attribute(argument.spelling)}"){default}')

    def parse_enum(self, node):
        self.out(f'py::enum_<{self.name(node)}>({self.module}, "{self.format_type(node.spelling)}", py::arithmetic())')
        self.out.indent += 1
        for value in node.get_children():
            self.out(f'.value("{self.format_enum(value.spelling)}", {value.spelling})')
        self.out('.export_values();')
        self.out.indent -= 1
        self.out('')

    def parse_constructor(self, node, cls):
        arguments = [a for a in node.get_arguments()]
        if len(arguments):
            self.out(f'{self.module_(cls)}.def(py::init<{self.arg_types(arguments)}>()')
            self.write_pyargs(arguments)
            self.out(');')
        else:
            self.out(f'{self.module_(cls)}.def(py::init<>());')

    def parse_field(self, node, cls):
        pyname = self.format_attribute(node.spelling)
        cname = self.name(node)
        if self.is_property_mappable(node):
            if self.is_property_readonly(node):
                self.out(f'{self.module_(cls)}.def_readonly("{pyname}", &{cname});')
            else:
                self.out(f'{self.module_(cls)}.def_readwrite("{pyname}", &{cname});')

    def should_wrap_function(self, node):
        if node.type.is_function_variadic():
            return True
        for arg in node.get_arguments():
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

    def get_function_return(self, node):
        returned = [a.spelling for a in node.get_arguments() if self.should_return_argument(a)]
        if not self.is_function_void_return(node):
            returned.insert(0, 'ret')
        if len(returned) > 1:
            return 'std::make_tuple({})'.format(', '.join(returned))
        if len(returned) == 1:
            return returned[0]
        return ''

    def get_return_policy(self, node):
        result = node.type.get_result()
        if result.kind == cindex.TypeKind.LVALUEREFERENCE:
            return 'py::return_value_policy::reference'
        else:
            return 'py::return_value_policy::automatic_reference'

    def parse_function(self, node, cls=None):
        if self.is_function_mappable(node):
            mname = self.module_(cls)
            arguments = [a for a in node.get_arguments()]
            cname = '&' + self.name(node)
            pyname = self.format_attribute(node.spelling)
            if self.is_overloaded(node):
                cname = f'py::overload_cast<{self.arg_types(arguments)}>({cname})'
            if self.should_wrap_function(node):
                self.out(f'{mname}.def("{pyname}", []({self.arg_string(arguments)})')
                self.out('{')
                ret = '' if self.is_function_void_return(node) else 'auto ret = '
                self.out(f'    {ret}{self.name(node)}({self.arg_names(arguments)});')
                self.out(f'    return {self.get_function_return(node)};')
                self.out('}')
            else:
                self.out(f'{mname}.def("{pyname}", {cname}')
            self.write_pyargs(arguments)
            self.out(f', {self.get_return_policy(node)});')

    def parse_class(self, node):
        if self.is_class_mappable(node):
            clsname = self.name(node)
            print(clsname)
            pyname = self.format_type(node.spelling)
            self.out(f'PYCLASS_BEGIN({self.module}, {clsname}, {pyname})')
            for child in node.get_children():
                print(child.kind, ':  ', child.spelling)
                if child.kind == cindex.CursorKind.CONSTRUCTOR:
                    self.parse_constructor(child, node)
                elif child.kind == cindex.CursorKind.CXX_METHOD:
                    self.parse_function(child, node)
                elif child.kind == cindex.CursorKind.FIELD_DECL:
                    self.parse_field(child, node)
            self.out(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')

    def parse_var(self, node):
        print(node.spelling)
        for child in node.get_children():
            print(child.spelling)

    def parse_definitions(self, node):
        for child in node.get_children():
            if not self.is_node_mappable(child):
                continue
            print(child.spelling, ':  ', child.kind)
            if child.kind == cindex.CursorKind.ENUM_DECL:
                self.parse_enum(child)
            elif child.kind == cindex.CursorKind.STRUCT_DECL:
                self.parse_class(child)
            elif child.kind == cindex.CursorKind.CLASS_DECL:
                self.parse_class(child)
            elif child.kind == cindex.CursorKind.VAR_DECL:
                self.parse_var(child)
            elif child.kind == cindex.CursorKind.FUNCTION_DECL:
                self.parse_function(child)
            elif child.kind == cindex.CursorKind.NAMESPACE:
                self.parse_definitions(child)

    def parse_overloads(self, node):
        for child in node.get_children():
            if child.kind in [cindex.CursorKind.CXX_METHOD, cindex.CursorKind.FUNCTION_DECL]:
                key = self.name(child)
                if key in self.overloaded.visited:
                    self.overloaded.add(key)
                else:
                    self.overloaded.visited.add(key)
            elif self.is_node_mappable(child):
                self.parse_overloads(child)

    def generate(self):
        if sys.platform == 'darwin':
            cindex.Config.set_library_path('/usr/local/opt/llvm@6/lib')
        elif sys.platform == 'linux':
            cindex.Config.set_library_file('libclang-10.so')
        else:
            cindex.Config.set_library_file('C:/Program Files/LLVM/bin/libclang.dll')
        '''
        if sys.platform == 'darwin':
            cindex.Config.set_library_path('/usr/local/opt/llvm@6/lib')
        elif sys.platform == 'win32':
            #cindex.Config.set_library_file('libclang.dll')
            cindex.Config.set_library_path('C:/Program Files/LLVM/bin')
        else:
            cindex.Config.set_library_file('libclang-10.so')
        '''
        BASE_PATH = pathlib.Path('.')
        path = BASE_PATH / self.source
        tu = cindex.Index.create().parse(path, args=self.flags)
        self.out.file = open(BASE_PATH / self.target, 'w')
        self.out.indent = 0
        self.out(self.header)
        self.out.indent = 1
        self.parse_overloads(tu.cursor)
        self.parse_definitions(tu.cursor)
        self.out.indent = 0
        self.out(self.footer)
