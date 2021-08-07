from clang import cindex

from .parser import Parser

class StructParser(Parser):
    def __init__(self, parent=None):
        super().__init__(parent)

    def parse_class_enum(self, node, clsname, pyname):
        #self.out(f'py::enum_<{self.name(node)}>({self.module}, "{self.format_type(node.spelling)}", py::arithmetic())')
        self.out(f'py::enum_<{self.name(node)}>({self.module}, "{pyname}", py::arithmetic())')
        #print(node.spelling)
        self.out.indent += 1
        for value in node.get_children():
            self.out(f'.value("{self.format_enum(value.spelling)}", {clsname}::Enum::{value.spelling})')
        self.out('.export_values();')
        self.out.indent -= 1
        self.out('')

    def parse(self, node):
        if self.is_class_mappable(node):
            clsname = self.name(node)
            pyname = self.format_type(node.spelling)
            first_child = list(node.get_children())[0]
            wrapped = first_child.spelling == 'Enum'
            if not wrapped:
              self.out(f'PYCLASS_BEGIN({self.module}, {clsname}, {pyname})')
            for child in node.get_children():
                if child.kind == cindex.CursorKind.CONSTRUCTOR:
                    self.parse_constructor(child, node)
                elif child.kind == cindex.CursorKind.CXX_METHOD:
                    self.parse_function(child, node)
                elif child.kind == cindex.CursorKind.FIELD_DECL:
                    self.parse_field(child, node)
                elif child.kind == cindex.CursorKind.ENUM_DECL:
                    self.parse_class_enum(child, clsname, pyname)

            if not wrapped:
              self.out(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')

        return self
    '''
    def parse(self, node):
        if self.is_class_mappable(node):
            clsname = self.name(node)
            print('STRUCT:  ', clsname)
            pyname = self.format_type(node.spelling)
            self.out(f'PYCLASS_BEGIN({self.module}, {clsname}, {pyname})')
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
            self.out(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')
        return self
    '''