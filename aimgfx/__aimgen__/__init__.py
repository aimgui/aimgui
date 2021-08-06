import toml

from aimgen.generator import GeneratorABC

HEADER = """
#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <aimgui/bindtools.h>

#include <bgfx/bgfx.h>
#include <bx/allocator.h>

using namespace bgfx;

namespace py = pybind11;

void init_generated(py::module &libaimgfx, Registry &registry) {
"""

FOOTER = """
}
"""

DEFAULTS = {
    '_layoutHandle' : 'std::initializer_list<int>(BGFX_INVALID_HANDLE)',
    '_init' : 'std::initializer_list<int>({})'
}

class Generator(GeneratorABC):
    def __init__(self, *config, **kwargs):
        super().__init__(*config, **kwargs)

    @classmethod
    def create(self, filename="aimgen.toml"):
        config = toml.load(filename)
        instance = Generator(config)
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
