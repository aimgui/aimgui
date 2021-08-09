from clang import cindex

from .transpiler_base import TranspilerBase

class Transpiler(TranspilerBase):
    def __init__(self):
        super().__init__()

    def parse_enum(self, node):
        self.scope(f'py::enum_<{self.spell(node)}>({self.module}, "{self.format_type(node.spelling)}", py::arithmetic())')
        self.scope.indent += 1
        for value in node.get_children():
            self.scope(f'.value("{self.format_enum(value.spelling)}", {value.spelling})')
        self.scope('.export_values();')
        self.scope.indent -= 1
        self.scope('')

    def parse_constructor(self, node, cls):
        arguments = [a for a in node.get_arguments()]
        if len(arguments):
            self.scope(f'{self.module_(cls)}.def(py::init<{self.arg_types(arguments)}>()')
            self.write_pyargs(arguments)
            self.scope(');')
        else:
            self.scope(f'{self.module_(cls)}.def(py::init<>());')

    def parse_field(self, node, cls):
        pyname = self.format_attribute(node.spelling)
        cname = self.spell(node)
        if self.is_property_mappable(node):
            if self.is_property_readonly(node):
                self.scope(f'{self.module_(cls)}.def_readonly("{pyname}", &{cname});')
            else:
                self.scope(f'{self.module_(cls)}.def_readwrite("{pyname}", &{cname});')

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
        #print(node.spelling)
        if self.is_function_mappable(node):
            mname = self.module_(cls)
            arguments = [a for a in node.get_arguments()]
            cname = '&' + self.spell(node)
            pyname = self.format_attribute(node.spelling)
            if self.is_overloaded(node):
                cname = f'py::overload_cast<{self.arg_types(arguments)}>({cname})'
            if self.should_wrap_function(node):
                self.scope(f'{mname}.def("{pyname}", []({self.arg_string(arguments)})')
                self.scope('{')
                ret = '' if self.is_function_void_return(node) else 'auto ret = '
                self.scope(f'    {ret}{self.spell(node)}({self.arg_names(arguments)});')
                self.scope(f'    return {self.get_function_return(node)};')
                self.scope('}')
            else:
                self.scope(f'{mname}.def("{pyname}", {cname}')
            self.write_pyargs(arguments)
            self.scope(f', {self.get_return_policy(node)});')

    def parse_struct_enum(self, node, clsname, pyname):
        #self.scope(f'py::enum_<{self.spell(node)}>({self.module}, "{self.format_type(node.spelling)}", py::arithmetic())')
        self.scope(f'py::enum_<{self.spell(node)}>({self.module}, "{pyname}", py::arithmetic())')
        #print(node.spelling)
        self.scope.indent += 1
        for value in node.get_children():
            self.scope(f'.value("{self.format_enum(value.spelling)}", {clsname}::Enum::{value.spelling})')
        self.scope('.export_values();')
        self.scope.indent -= 1
        self.scope('')

    def parse_struct(self, node):
        if self.is_class_mappable(node):
            clsname = self.spell(node)
            pyname = self.format_type(node.spelling)
            children = list(node.get_children()) # it's an iterator
            wrapped = False
            #Handle the case of a struct with one enum child
            if len(children) == 1:
                first_child = children[0]
                wrapped = first_child.kind == cindex.CursorKind.ENUM_DECL
            if not wrapped:
              self.scope(f'PYCLASS_BEGIN({self.module}, {clsname}, {pyname})')
            for child in node.get_children():
                if child.kind == cindex.CursorKind.CONSTRUCTOR:
                    self.parse_constructor(child, node)
                elif child.kind == cindex.CursorKind.CXX_METHOD:
                    self.parse_function(child, node)
                elif child.kind == cindex.CursorKind.FIELD_DECL:
                    self.parse_field(child, node)
                elif child.kind == cindex.CursorKind.ENUM_DECL:
                    self.parse_struct_enum(child, clsname, pyname)

            if not wrapped:
              self.scope(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')

    def parse_class(self, node):
        if self.is_class_mappable(node):
            clsname = self.name(node)
            #print(clsname)
            pyname = self.format_type(node.spelling)
            self.scope(f'PYCLASS_BEGIN({self.module}, {clsname}, {pyname})')
            for child in node.get_children():
                #print(child.kind, ':  ', child.spelling)
                if child.kind == cindex.CursorKind.CONSTRUCTOR:
                    self.parse_constructor(child, node)
                elif child.kind == cindex.CursorKind.FUNCTION_DECL:
                    self.parse_function(child, node)
                elif child.kind == cindex.CursorKind.CXX_METHOD:
                    self.parse_function(child, node)
                elif child.kind == cindex.CursorKind.FIELD_DECL:
                    self.parse_field(child, node)
            self.scope(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')

    def parse_var(self, node):
        print(f'Not implemented:  parse_var: {node.spelling}')

    def dispatch(self, node):
        self.actions[node.kind](self, node)

    def parse_definitions(self, node):
        for child in node.get_children():
            if not self.is_node_mappable(child):
                continue
            #print(child.spelling, ':  ', child.kind)
            kind = child.kind
            if kind in self.actions:
                self.dispatch(child)
            elif kind == cindex.CursorKind.ENUM_DECL:
                self.parse_enum(child)
            elif kind == cindex.CursorKind.VAR_DECL:
                self.parse_var(child)
            elif kind == cindex.CursorKind.FUNCTION_DECL:
                self.parse_function(child)
            elif kind == cindex.CursorKind.NAMESPACE:
                self.parse_definitions(child)
            elif kind == cindex.CursorKind.UNEXPOSED_DECL:
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
