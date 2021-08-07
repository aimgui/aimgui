from clang import cindex

from aimgen.struct_parser import StructParser
from aimgen.class_parser import ClassParser

MAP = {
    cindex.CursorKind.STRUCT_DECL : lambda dispatcher, node : StructParser(dispatcher).parse(node),
    cindex.CursorKind.CLASS_DECL : lambda dispatcher, node : ClassParser(dispatcher).parse(node)
}