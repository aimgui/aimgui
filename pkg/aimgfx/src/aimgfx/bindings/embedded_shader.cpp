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
    PYCLASS_BEGIN(libaimgfx, bgfx::EmbeddedShader, EmbeddedShader)
    EmbeddedShader.def_readwrite("name", &bgfx::EmbeddedShader::name);
    EmbeddedShader.def_readonly("data", &bgfx::EmbeddedShader::data);
    PYCLASS_END(libaimgfx, bgfx::EmbeddedShader, EmbeddedShader)

    libaimgfx.def("create_embedded_shader", &bgfx::createEmbeddedShader
    , py::arg("_es")
    , py::arg("_type")
    , py::arg("_name")
    , py::return_value_policy::automatic_reference);

}