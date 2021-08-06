class Parse:
    def __init__(node):
        pass

class ParseRoot(Parse):
    def __init__(node):
        pass

    def parse(self, node):
        for child in node.get_children():
            if not self.is_node_mappable(child):
                continue
            if child.kind == cindex.CursorKind.ENUM_DECL:
                self.parse_enum(child)
            elif child.kind == cindex.CursorKind.STRUCT_DECL:
                self.parse_class(child)
            elif child.kind == cindex.CursorKind.FUNCTION_DECL:
                self.parse_function(child)
            elif child.kind == cindex.CursorKind.NAMESPACE:
                self.parse_definitions(child)

