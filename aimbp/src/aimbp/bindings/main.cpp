#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "imgui.h"
#include "imgui_internal.h"

#include "imgui_node_editor.h"
#include "imgui_node_editor_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_main(py::module &libaimbp, Registry &registry) {

    /*
        EditorContext needs to be an opaque type.  Wrap it with PyCapsule
    */
    libaimbp.def("set_current_editor",  [](py::capsule& ctx)
    {
        ax::NodeEditor::SetCurrentEditor(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_current_editor", []()
    {
        return py::capsule(ax::NodeEditor::GetCurrentEditor(), "ImBpEditorContext");
    }
    , py::return_value_policy::automatic_reference);
    /*
    libaimbp.def("create_editor", [](py::capsule& config)
    {
        return py::capsule(ax::NodeEditor::CreateEditor(config), "ImBpEditorContext");
    }
    , py::arg("config") = nullptr
    , py::return_value_policy::automatic_reference);
    */
    libaimbp.def("create_editor", []()
    {
        return py::capsule(ax::NodeEditor::CreateEditor(), "ImBpEditorContext");
    }
    , py::return_value_policy::automatic_reference);

    libaimbp.def("destroy_editor", [](py::capsule& ctx)
    {
        ax::NodeEditor::DestroyEditor(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
    /*
    libaimbp.def("query_new_link", py::overload_cast<ax::NodeEditor::PinId *, ax::NodeEditor::PinId *, const ImVec4 &, float>(&ax::NodeEditor::QueryNewLink)
    , py::arg("start_id")
    , py::arg("end_id")
    , py::arg("color") = ImVec4(1,1,1,1)
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    */
    libaimbp.def("query_new_link",  [](const ImVec4& color, float thickness)
    {
        ax::NodeEditor::PinId pin1, pin2;
        bool success = ax::NodeEditor::QueryNewLink(&pin1, &pin2, color, thickness);
        auto result = py::make_tuple(success, pin1.Get(), pin2.Get());
        return result;
    }
    , py::arg("color") = ImVec4(1,1,1,1)
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);

}

