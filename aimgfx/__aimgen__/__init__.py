from clang import cindex

import toml

from aimgen.generator import GeneratorBase

HEADER = """
#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <aimgui/bindtools.h>

#include <aimgfx/aimgfx.h>
#include <bx/allocator.h>

using namespace bgfx;

namespace py = pybind11;

void init_generated(py::module &libaimgfx, Registry &registry) {
"""

FOOTER = """
}
"""

DEFAULTS = {
    '_layoutHandle' : 'bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)',
    '_init' : 'bgfx::Init()'
}

class Generator(GeneratorBase):
    def __init__(self, *config, **kwargs):
        super().__init__(*config, **kwargs)

    @classmethod
    def create(self, filename="aimgen.toml"):
        config = toml.load(filename)
        instance = Generator(config)
        instance.import_factories()
        return instance

    @property
    def header(self):
        return HEADER

    @property
    def footer(self):
        return FOOTER

    @property
    def defaults(self):
        return DEFAULTS
    '''
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

    def parse_class(self, node):
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
                elif child.kind == cindex.CursorKind.STRUCT_DECL:
                    self.parse_class(child)

            if not wrapped:
              self.out(f'PYCLASS_END({self.module}, {clsname}, {pyname})\n')
    '''