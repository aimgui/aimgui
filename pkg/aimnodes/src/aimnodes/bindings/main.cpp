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

void init_main(py::module &_aimnodes, Registry &registry) {

    /*
        ImNodesContext needs to be an opaque type.  Wrap it with PyCapsule
    */
    //ImNodesContext* CreateContext();
    _aimnodes.def("create_context", []()
    {
        return py::capsule(ImNodes::CreateContext(), "ImNodesContext");
    }
    , py::return_value_policy::automatic_reference);

    //void            DestroyContext(ImNodesContext* ctx = NULL); // NULL = destroy current context
    _aimnodes.def("destroy_context", [](py::capsule& ctx)
    {
        ImNodes::DestroyContext(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //ImNodesContext* GetCurrentContext();
    _aimnodes.def("get_current_context", []()
    {
        return (void*)ImNodes::GetCurrentContext();
    }
    , py::return_value_policy::automatic_reference);

    //void            SetCurrentContext(ImNodesContext* ctx);
    _aimnodes.def("set_current_context", [](py::capsule& ctx)
    {
        ImNodes::SetCurrentContext(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

    //EditorContext needs to be an opaque type.  Wrap it with PyCapsule
    //EditorContext* EditorContextCreate()
    _aimnodes.def("editor_context_create", []()
    {
        return py::capsule(ImNodes::EditorContextCreate(), "ImNodesEditorContext");
    }
    , py::return_value_policy::automatic_reference);

    //void EditorContextFree(EditorContext* ctx)
    _aimnodes.def("editor_context_free", [](py::capsule& ctx)
    {
        ImNodes::EditorContextFree(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //void EditorContextSet(EditorContext*);
    _aimnodes.def("editor_context_set", [](py::capsule& ctx)
    {
        ImNodes::EditorContextSet(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

/*
void MiniMap(
    const float                              minimap_size_fraction = 0.2f,
    const ImNodesMiniMapLocation             location = ImNodesMiniMapLocation_TopLeft,
    const ImNodesMiniMapNodeHoveringCallback node_hovering_callback = NULL,
    void*                                    node_hovering_callback_data = NULL);
*/
    _aimnodes.def("mini_map",
      [](const float minimap_size_fraction,
        const ImNodesMiniMapLocation location,
        const ImNodesMiniMapNodeHoveringCallback node_hovering_callback,
        const ImNodesMiniMapNodeHoveringCallbackUserData node_hovering_callback_data) {
            return ImNodes::MiniMap(minimap_size_fraction, location, node_hovering_callback, node_hovering_callback_data);
            /*if (node_hovering_callback.is_none())
                return ImNodes::MiniMap(minimap_size_fraction, location, py::function(), node_hovering_callback_data);
            else
                return ImNodes::MiniMap(minimap_size_fraction, location, py::function(node_hovering_callback), node_hovering_callback_data);*/
                
      }
      , py::arg("size_fraction") = 0.2f
      , py::arg("location") = int(ImNodesMiniMapLocation_TopLeft)
      , py::arg("hovering_callback") = nullptr
      , py::arg("hovering_callback_data") = nullptr
      , py::return_value_policy::automatic_reference);

    /*_aimnodes.def("mini_map",
      [](const float                              minimap_size_fraction = 0.2f,
        const ImNodesMiniMapLocation             location = ImNodesMiniMapLocation_TopLeft) {
          return ImNodes::MiniMap(minimap_size_fraction, location);
      }
      , py::arg("size_fraction")
      , py::arg("location")
      , py::return_value_policy::automatic_reference);*/
}

