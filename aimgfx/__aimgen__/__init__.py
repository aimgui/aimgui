from clang import cindex

import os
import toml
from pathlib import Path
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
    def create(self, name="aimgen"):
        filename = f'{name}.toml'
        path = Path(os.getcwd(), '__aimgen__', filename)
        print(path)
        config = toml.load(path)
        config['name'] = name
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
