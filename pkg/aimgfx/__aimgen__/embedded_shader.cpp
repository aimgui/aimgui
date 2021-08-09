#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <aimgui/bindtools.h>

#include <aimgfx/aimgfx.h>
#include <bx/allocator.h>
#include <bgfx/embedded_shader.h>

using namespace bgfx;

namespace py = pybind11;

void init_embedded_shader(py::module &libaimgfx, Registry &registry) {
{{body}}
}
