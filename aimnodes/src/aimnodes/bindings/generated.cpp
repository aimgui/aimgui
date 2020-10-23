
#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include "imgui.h"
#include "imgui_internal.h"

#include "imnodes.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

using namespace imnodes;

void init_generated(py::module &libaimnodes, Registry &registry) {

    py::enum_<imnodes::ColorStyle>(libaimnodes, "ColorStyle", py::arithmetic())
        .value("COLOR_STYLE_NODE_BACKGROUND", ColorStyle_NodeBackground)
        .value("COLOR_STYLE_NODE_BACKGROUND_HOVERED", ColorStyle_NodeBackgroundHovered)
        .value("COLOR_STYLE_NODE_BACKGROUND_SELECTED", ColorStyle_NodeBackgroundSelected)
        .value("COLOR_STYLE_NODE_OUTLINE", ColorStyle_NodeOutline)
        .value("COLOR_STYLE_TITLE_BAR", ColorStyle_TitleBar)
        .value("COLOR_STYLE_TITLE_BAR_HOVERED", ColorStyle_TitleBarHovered)
        .value("COLOR_STYLE_TITLE_BAR_SELECTED", ColorStyle_TitleBarSelected)
        .value("COLOR_STYLE_LINK", ColorStyle_Link)
        .value("COLOR_STYLE_LINK_HOVERED", ColorStyle_LinkHovered)
        .value("COLOR_STYLE_LINK_SELECTED", ColorStyle_LinkSelected)
        .value("COLOR_STYLE_PIN", ColorStyle_Pin)
        .value("COLOR_STYLE_PIN_HOVERED", ColorStyle_PinHovered)
        .value("COLOR_STYLE_BOX_SELECTOR", ColorStyle_BoxSelector)
        .value("COLOR_STYLE_BOX_SELECTOR_OUTLINE", ColorStyle_BoxSelectorOutline)
        .value("COLOR_STYLE_GRID_BACKGROUND", ColorStyle_GridBackground)
        .value("COLOR_STYLE_GRID_LINE", ColorStyle_GridLine)
        .value("COLOR_STYLE_COUNT", ColorStyle_Count)
        .export_values();

    py::enum_<imnodes::StyleVar>(libaimnodes, "StyleVar", py::arithmetic())
        .value("STYLE_VAR_GRID_SPACING", StyleVar_GridSpacing)
        .value("STYLE_VAR_NODE_CORNER_ROUNDING", StyleVar_NodeCornerRounding)
        .value("STYLE_VAR_NODE_PADDING_HORIZONTAL", StyleVar_NodePaddingHorizontal)
        .value("STYLE_VAR_NODE_PADDING_VERTICAL", StyleVar_NodePaddingVertical)
        .export_values();

    py::enum_<imnodes::StyleFlags>(libaimnodes, "StyleFlags", py::arithmetic())
        .value("STYLE_FLAGS_NONE", StyleFlags_None)
        .value("STYLE_FLAGS_NODE_OUTLINE", StyleFlags_NodeOutline)
        .value("STYLE_FLAGS_GRID_LINES", StyleFlags_GridLines)
        .export_values();

    py::enum_<imnodes::PinShape>(libaimnodes, "PinShape", py::arithmetic())
        .value("PIN_SHAPE_CIRCLE", PinShape_Circle)
        .value("PIN_SHAPE_CIRCLE_FILLED", PinShape_CircleFilled)
        .value("PIN_SHAPE_TRIANGLE", PinShape_Triangle)
        .value("PIN_SHAPE_TRIANGLE_FILLED", PinShape_TriangleFilled)
        .value("PIN_SHAPE_QUAD", PinShape_Quad)
        .value("PIN_SHAPE_QUAD_FILLED", PinShape_QuadFilled)
        .export_values();

    py::enum_<imnodes::AttributeFlags>(libaimnodes, "AttributeFlags", py::arithmetic())
        .value("ATTRIBUTE_FLAGS_NONE", AttributeFlags_None)
        .value("ATTRIBUTE_FLAGS_ENABLE_LINK_DETACH_WITH_DRAG_CLICK", AttributeFlags_EnableLinkDetachWithDragClick)
        .value("ATTRIBUTE_FLAGS_ENABLE_LINK_CREATION_ON_SNAP", AttributeFlags_EnableLinkCreationOnSnap)
        .export_values();

    PYCLASS_BEGIN(libaimnodes, imnodes::IO, IO)
    IO.def_readwrite("emulate_three_button_mouse", &imnodes::IO::emulate_three_button_mouse);
    IO.def_readwrite("link_detach_with_modifier_click", &imnodes::IO::link_detach_with_modifier_click);
    IO.def(py::init<>());
    PYCLASS_END(libaimnodes, imnodes::IO, IO)

    PYCLASS_BEGIN(libaimnodes, imnodes::Style, Style)
    Style.def_readwrite("grid_spacing", &imnodes::Style::grid_spacing);
    Style.def_readwrite("node_corner_rounding", &imnodes::Style::node_corner_rounding);
    Style.def_readwrite("node_padding_horizontal", &imnodes::Style::node_padding_horizontal);
    Style.def_readwrite("node_padding_vertical", &imnodes::Style::node_padding_vertical);
    Style.def_readwrite("link_thickness", &imnodes::Style::link_thickness);
    Style.def_readwrite("link_line_segments_per_length", &imnodes::Style::link_line_segments_per_length);
    Style.def_readwrite("link_hover_distance", &imnodes::Style::link_hover_distance);
    Style.def_readwrite("pin_circle_radius", &imnodes::Style::pin_circle_radius);
    Style.def_readwrite("pin_quad_side_length", &imnodes::Style::pin_quad_side_length);
    Style.def_readwrite("pin_triangle_side_length", &imnodes::Style::pin_triangle_side_length);
    Style.def_readwrite("pin_line_thickness", &imnodes::Style::pin_line_thickness);
    Style.def_readwrite("pin_hover_radius", &imnodes::Style::pin_hover_radius);
    Style.def_readwrite("pin_offset", &imnodes::Style::pin_offset);
    Style.def_readwrite("flags", &imnodes::Style::flags);
    Style.def_readonly("colors", &imnodes::Style::colors);
    Style.def(py::init<>());
    PYCLASS_END(libaimnodes, imnodes::Style, Style)

    libaimnodes.def("editor_context_get_panning", &imnodes::EditorContextGetPanning
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("editor_context_reset_panning", &imnodes::EditorContextResetPanning
    , py::arg("pos")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("editor_context_move_to_node", &imnodes::EditorContextMoveToNode
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("initialize", &imnodes::Initialize
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("shutdown", &imnodes::Shutdown
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_io", &imnodes::GetIO
    , py::return_value_policy::reference);
    libaimnodes.def("get_style", &imnodes::GetStyle
    , py::return_value_policy::reference);
    libaimnodes.def("style_colors_dark", &imnodes::StyleColorsDark
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("style_colors_classic", &imnodes::StyleColorsClassic
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("style_colors_light", &imnodes::StyleColorsLight
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_node_editor", &imnodes::BeginNodeEditor
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_node_editor", &imnodes::EndNodeEditor
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("push_color_style", &imnodes::PushColorStyle
    , py::arg("item")
    , py::arg("color")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("pop_color_style", &imnodes::PopColorStyle
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("push_style_var", &imnodes::PushStyleVar
    , py::arg("style_item")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("pop_style_var", &imnodes::PopStyleVar
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_node", &imnodes::BeginNode
    , py::arg("id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_node", &imnodes::EndNode
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_node_dimensions", &imnodes::GetNodeDimensions
    , py::arg("id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_node_title_bar", &imnodes::BeginNodeTitleBar
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_node_title_bar", &imnodes::EndNodeTitleBar
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_input_attribute", &imnodes::BeginInputAttribute
    , py::arg("id")
    , py::arg("shape") = PinShape_CircleFilled
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_input_attribute", &imnodes::EndInputAttribute
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_output_attribute", &imnodes::BeginOutputAttribute
    , py::arg("id")
    , py::arg("shape") = PinShape_CircleFilled
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_output_attribute", &imnodes::EndOutputAttribute
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("begin_static_attribute", &imnodes::BeginStaticAttribute
    , py::arg("id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("end_static_attribute", &imnodes::EndStaticAttribute
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("push_attribute_flag", &imnodes::PushAttributeFlag
    , py::arg("flag")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("pop_attribute_flag", &imnodes::PopAttributeFlag
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("link", &imnodes::Link
    , py::arg("id")
    , py::arg("start_attribute_id")
    , py::arg("end_attribute_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("set_node_screen_space_pos", &imnodes::SetNodeScreenSpacePos
    , py::arg("node_id")
    , py::arg("screen_space_pos")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("set_node_editor_space_pos", &imnodes::SetNodeEditorSpacePos
    , py::arg("node_id")
    , py::arg("editor_space_pos")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("set_node_grid_space_pos", &imnodes::SetNodeGridSpacePos
    , py::arg("node_id")
    , py::arg("grid_pos")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("set_node_draggable", &imnodes::SetNodeDraggable
    , py::arg("node_id")
    , py::arg("draggable")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_node_screen_space_pos", &imnodes::GetNodeScreenSpacePos
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_node_editor_space_pos", &imnodes::GetNodeEditorSpacePos
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_node_grid_space_pos", &imnodes::GetNodeGridSpacePos
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_editor_hovered", &imnodes::IsEditorHovered
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_node_hovered", [](int * node_id)
    {
        auto ret = imnodes::IsNodeHovered(node_id);
        return std::make_tuple(ret, node_id);
    }
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_hovered", [](int * link_id)
    {
        auto ret = imnodes::IsLinkHovered(link_id);
        return std::make_tuple(ret, link_id);
    }
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_pin_hovered", [](int * attribute_id)
    {
        auto ret = imnodes::IsPinHovered(attribute_id);
        return std::make_tuple(ret, attribute_id);
    }
    , py::arg("attribute_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("num_selected_nodes", &imnodes::NumSelectedNodes
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("num_selected_links", &imnodes::NumSelectedLinks
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_selected_nodes", [](int * node_ids)
    {
        imnodes::GetSelectedNodes(node_ids);
        return node_ids;
    }
    , py::arg("node_ids")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("get_selected_links", [](int * link_ids)
    {
        imnodes::GetSelectedLinks(link_ids);
        return link_ids;
    }
    , py::arg("link_ids")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_attribute_active", &imnodes::IsAttributeActive
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_any_attribute_active", [](int * attribute_id)
    {
        auto ret = imnodes::IsAnyAttributeActive(attribute_id);
        return std::make_tuple(ret, attribute_id);
    }
    , py::arg("attribute_id") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_started", [](int * started_at_attribute_id)
    {
        auto ret = imnodes::IsLinkStarted(started_at_attribute_id);
        return std::make_tuple(ret, started_at_attribute_id);
    }
    , py::arg("started_at_attribute_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_dropped", [](int * started_at_attribute_id, bool including_detached_links)
    {
        auto ret = imnodes::IsLinkDropped(started_at_attribute_id, including_detached_links);
        return std::make_tuple(ret, started_at_attribute_id);
    }
    , py::arg("started_at_attribute_id") = nullptr
    , py::arg("including_detached_links") = true
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_created", [](int * started_at_attribute_id, int * ended_at_attribute_id, bool * created_from_snap)
    {
        auto ret = imnodes::IsLinkCreated(started_at_attribute_id, ended_at_attribute_id, created_from_snap);
        return std::make_tuple(ret, started_at_attribute_id, ended_at_attribute_id, created_from_snap);
    }
    , py::arg("started_at_attribute_id")
    , py::arg("ended_at_attribute_id")
    , py::arg("created_from_snap") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_created", [](int * started_at_node_id, int * started_at_attribute_id, int * ended_at_node_id, int * ended_at_attribute_id, bool * created_from_snap)
    {
        auto ret = imnodes::IsLinkCreated(started_at_node_id, started_at_attribute_id, ended_at_node_id, ended_at_attribute_id, created_from_snap);
        return std::make_tuple(ret, started_at_node_id, started_at_attribute_id, ended_at_node_id, ended_at_attribute_id, created_from_snap);
    }
    , py::arg("started_at_node_id")
    , py::arg("started_at_attribute_id")
    , py::arg("ended_at_node_id")
    , py::arg("ended_at_attribute_id")
    , py::arg("created_from_snap") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("is_link_destroyed", [](int * link_id)
    {
        auto ret = imnodes::IsLinkDestroyed(link_id);
        return std::make_tuple(ret, link_id);
    }
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("save_current_editor_state_to_ini_string", [](size_t * data_size)
    {
        auto ret = imnodes::SaveCurrentEditorStateToIniString(data_size);
        return std::make_tuple(ret, data_size);
    }
    , py::arg("data_size") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("load_current_editor_state_from_ini_string", &imnodes::LoadCurrentEditorStateFromIniString
    , py::arg("data")
    , py::arg("data_size")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("save_current_editor_state_to_ini_file", &imnodes::SaveCurrentEditorStateToIniFile
    , py::arg("file_name")
    , py::return_value_policy::automatic_reference);
    libaimnodes.def("load_current_editor_state_from_ini_file", &imnodes::LoadCurrentEditorStateFromIniFile
    , py::arg("file_name")
    , py::return_value_policy::automatic_reference);

}

