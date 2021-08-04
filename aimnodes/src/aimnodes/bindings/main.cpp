#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "imgui.h"
#include "imgui_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

#include "imnodes.h"
#include "imnodes_internal.h"

//TODO:Why did I have to put this here?  Getting an external reference error
char ImGuiTextBuffer::EmptyString[1] = { 0 };

namespace py = pybind11;

void init_main(py::module &libaimnodes, Registry &registry) {

    /*
        ImNodesContext needs to be an opaque type.  Wrap it with PyCapsule
    */
    //ImNodesContext* CreateContext();
    libaimnodes.def("create_context", []()
    {
        return py::capsule(ImNodes::CreateContext(), "ImNodesContext");
    }
    , py::return_value_policy::automatic_reference);

    //void            DestroyContext(ImNodesContext* ctx = NULL); // NULL = destroy current context
    libaimnodes.def("destroy_context", [](py::capsule& ctx)
    {
        ImNodes::DestroyContext(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //ImNodesContext* GetCurrentContext();
    libaimnodes.def("get_current_context", []()
    {
        return (void*)ImNodes::GetCurrentContext();
    }
    , py::return_value_policy::automatic_reference);

    //void            SetCurrentContext(ImNodesContext* ctx);
    libaimnodes.def("set_current_context", [](py::capsule& ctx)
    {
        ImNodes::SetCurrentContext(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

    //EditorContext needs to be an opaque type.  Wrap it with PyCapsule
    //EditorContext* EditorContextCreate()
    libaimnodes.def("editor_context_create", []()
    {
        return py::capsule(ImNodes::EditorContextCreate(), "ImNodesEditorContext");
    }
    , py::return_value_policy::automatic_reference);

    //void EditorContextFree(EditorContext* ctx)
    libaimnodes.def("editor_context_free", [](py::capsule& ctx)
    {
        ImNodes::EditorContextFree(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //void EditorContextSet(EditorContext*);
    libaimnodes.def("editor_context_set", [](py::capsule& ctx)
    {
        ImNodes::EditorContextSet(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
}

