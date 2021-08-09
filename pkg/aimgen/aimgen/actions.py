from clang import cindex

MAP = {
    cindex.CursorKind.STRUCT_DECL : lambda self, node : self.parse_struct(node),
    cindex.CursorKind.CLASS_DECL : lambda self, node : self.parse_class(node)
}