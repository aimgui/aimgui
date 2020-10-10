from generate.generator import Generator

HEADER = """
#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <limits>
#include "imgui.h"
#include "imgui_internal.h"

#include <aimgui/conversions.h>
#include "bindtools.h"

namespace py = pybind11;

void init_generated(py::module &libaimgui, Registry &registry) {
"""

FOOTER = """
}
"""

class ImGuiGenerator(Generator):
    pass