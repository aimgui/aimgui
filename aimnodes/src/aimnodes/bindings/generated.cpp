
#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include "imgui.h"
#include "imgui_internal.h"

#include "imgui_node_editor.h"
#include "imgui_node_editor_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

#include <aimbp/conversions.h>

namespace py = pybind11;

using namespace ax::NodeEditor;

void init_generated(py::module &libaimbp, Registry &registry) {


}

