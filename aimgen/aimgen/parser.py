import re

from clang import cindex

from . import UserSet

def snakecase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Out:
    def __init__(self):
        self.indent = 0

class StringOut(Out):
    def __init__(self, string=''):
        super().__init__()
        self.string = string

    def __call__(self, line):
        if len(line):
            self.string += ' ' * self.indent * 4
            self.string += line.replace('>>', '> >')
        self.string += '\n'

class FileOut(Out):
    def __init__(self, file):
        super().__init__()
        self.file = file

    def __call__(self, line):
        if len(line):
            self.file.write(' ' * self.indent * 4)
            self.file.write(line.replace('>>', '> >'))
        self.file.write('\n')

class Parser:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        #
        self.out = StringOut()
        #
        # Injected members
        # TODO: Validate after injection
        #
        self.source = ''
        self.mapped = ''
        self.target = ''
        self.prefix = ''
        self.short_prefix = ''
        self.module = ''
        self.flags = []
        self.excludes = []
        self.overloaded = []
        self.defaults = {}
        # End Injected members
        if self.parent:
            self.parent.add_child(self)
            self.config = parent.config
            for key in self.config:
                setattr(self, key, self.config[key])
            self.options = parent.options
            self.overloaded = parent.overloaded
            self.excludes = parent.excludes
            self.defaults = parent.defaults
            self.out.indent = parent.out.indent


    def add_child(self, child):
        self.children.append(child)

    def write(self, out):
        out(self.out.string)
        for child in self.children:
            child.write(out)

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
        if self.spell(node) in self.excludes:
            return True
        if node.spelling.startswith('_'):
            return True
        return False

    def spell(self, node):
        if node is None:
            return ''
        elif node.kind == cindex.CursorKind.TRANSLATION_UNIT:
            return ''
        else:
            res = self.spell(node.semantic_parent)
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
        return self.spell(node) in self.overloaded

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
        self.out(f'py::enum_<{self.spell(node)}>({self.module}, "{self.format_type(node.spelling)}", py::arithmetic())')
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
        cname = self.spell(node)
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
            cname = '&' + self.spell(node)
            pyname = self.format_attribute(node.spelling)
            if self.is_overloaded(node):
                cname = f'py::overload_cast<{self.arg_types(arguments)}>({cname})'
            if self.should_wrap_function(node):
                self.out(f'{mname}.def("{pyname}", []({self.arg_string(arguments)})')
                self.out('{')
                ret = '' if self.is_function_void_return(node) else 'auto ret = '
                self.out(f'    {ret}{self.spell(node)}({self.arg_names(arguments)});')
                self.out(f'    return {self.get_function_return(node)};')
                self.out('}')
            else:
                self.out(f'{mname}.def("{pyname}", {cname}')
            self.write_pyargs(arguments)
            self.out(f', {self.get_return_policy(node)});')

    def parse_var(self, node):
        print(node.spelling)
        for child in node.get_children():
            print(child.spelling)

    def dispatch(self, node):
        parser = self.factories[node.kind](self, node)
        #self.write(parser.out)
        self.out(parser.out.string)

    def parse_definitions(self, node):
        for child in node.get_children():
            if not self.is_node_mappable(child):
                continue
            #print(child.spelling, ':  ', child.kind)
            kind = child.kind
            if kind in self.factories:
                self.dispatch(child)
            elif kind == cindex.CursorKind.ENUM_DECL:
                self.parse_enum(child)
            elif kind == cindex.CursorKind.VAR_DECL:
                self.parse_var(child)
            elif kind == cindex.CursorKind.FUNCTION_DECL:
                self.parse_function(child)
            elif kind == cindex.CursorKind.NAMESPACE:
                self.parse_definitions(child)

    def parse_overloads(self, node):
        for child in node.get_children():
            if child.kind in [cindex.CursorKind.CXX_METHOD, cindex.CursorKind.FUNCTION_DECL]:
                key = self.spell(child)
                if key in self.overloaded.visited:
                    self.overloaded.add(key)
                else:
                    self.overloaded.visited.add(key)
            elif self.is_node_mappable(child):
                self.parse_overloads(child)
