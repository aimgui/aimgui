#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include <aim/bindtools.h>

#include <bgfx/bgfx.h>

using namespace bgfx;

namespace py = pybind11;

void init_main(py::module &libaimgfx, Registry &registry) {
}

