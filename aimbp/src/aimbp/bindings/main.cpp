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
    libaimbp.def("create_editor", [](py::capsule& config)
    {
        return py::capsule(ax::NodeEditor::CreateEditor(config), "ImBpEditorContext");
    }
    , py::arg("config") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimbp.def("destroy_editor", [](py::capsule& ctx)
    {
        ax::NodeEditor::DestroyEditor(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

   /*
    //EditorContext* EditorContextCreate()
    libaimbp.def("editor_context_create", []()
    {
        return py::capsule(imnodes::EditorContextCreate(), "ImNodesEditorContext");
    }
    , py::return_value_policy::automatic_reference);

    //void EditorContextFree(EditorContext* ctx)
    libaimbp.def("editor_context_free", [](py::capsule& ctx)
    {
        imnodes::EditorContextFree(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //void EditorContextSet(EditorContext*);
    libaimbp.def("editor_context_set", [](py::capsule& ctx)
    {
        imnodes::EditorContextSet(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
    */
}

