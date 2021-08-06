from clang import cindex

from aimgen.struct_parser import StructParser
from aimgen.class_parser import ClassParser

MAP = {
    cindex.CursorKind.STRUCT_DECL : lambda parent : StructParser(parent),
    cindex.CursorKind.CLASS_DECL : lambda parent : ClassParser(parent)
}