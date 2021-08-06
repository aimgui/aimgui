from clang import cindex

from .parser import Parser

class ClassParser(Parser):
    def __init__(self, parent=None):
        super().__init__(parent)

    def parse(self, node):
        if self.is_class_mappable(node):
            clsname = self.name(node)
            #print(clsname)
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
