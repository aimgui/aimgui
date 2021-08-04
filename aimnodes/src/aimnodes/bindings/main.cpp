#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "imnodes.h"
#include "imnodes_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_main(py::module &libaimnodes, Registry &registry) {

    
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

