
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

    py::enum_<ax::NodeEditor::SaveReasonFlags>(libaimbp, "SaveReasonFlags", py::arithmetic())
        .value("NONE", ax::NodeEditor::SaveReasonFlags::None)
        .value("NAVIGATION", ax::NodeEditor::SaveReasonFlags::Navigation)
        .value("POSITION", ax::NodeEditor::SaveReasonFlags::Position)
        .value("SIZE", ax::NodeEditor::SaveReasonFlags::Size)
        .value("SELECTION", ax::NodeEditor::SaveReasonFlags::Selection)
        .value("USER", ax::NodeEditor::SaveReasonFlags::User)
        .export_values();

    py::enum_<ax::NodeEditor::PinKind>(libaimbp, "PinKind", py::arithmetic())
        .value("INPUT", ax::NodeEditor::PinKind::Input)
        .value("OUTPUT", ax::NodeEditor::PinKind::Output)
        .export_values();

    py::enum_<ax::NodeEditor::StyleColor>(libaimbp, "StyleColor", py::arithmetic())
        .value("STYLE_COLOR_BG", ax::NodeEditor::StyleColor::StyleColor_Bg)
        .value("STYLE_COLOR_GRID", ax::NodeEditor::StyleColor::StyleColor_Grid)
        .value("STYLE_COLOR_NODE_BG", ax::NodeEditor::StyleColor::StyleColor_NodeBg)
        .value("STYLE_COLOR_NODE_BORDER", ax::NodeEditor::StyleColor::StyleColor_NodeBorder)
        .value("STYLE_COLOR_HOV_NODE_BORDER", ax::NodeEditor::StyleColor::StyleColor_HovNodeBorder)
        .value("STYLE_COLOR_SEL_NODE_BORDER", ax::NodeEditor::StyleColor::StyleColor_SelNodeBorder)
        .value("STYLE_COLOR_NODE_SEL_RECT", ax::NodeEditor::StyleColor::StyleColor_NodeSelRect)
        .value("STYLE_COLOR_NODE_SEL_RECT_BORDER", ax::NodeEditor::StyleColor::StyleColor_NodeSelRectBorder)
        .value("STYLE_COLOR_HOV_LINK_BORDER", ax::NodeEditor::StyleColor::StyleColor_HovLinkBorder)
        .value("STYLE_COLOR_SEL_LINK_BORDER", ax::NodeEditor::StyleColor::StyleColor_SelLinkBorder)
        .value("STYLE_COLOR_LINK_SEL_RECT", ax::NodeEditor::StyleColor::StyleColor_LinkSelRect)
        .value("STYLE_COLOR_LINK_SEL_RECT_BORDER", ax::NodeEditor::StyleColor::StyleColor_LinkSelRectBorder)
        .value("STYLE_COLOR_PIN_RECT", ax::NodeEditor::StyleColor::StyleColor_PinRect)
        .value("STYLE_COLOR_PIN_RECT_BORDER", ax::NodeEditor::StyleColor::StyleColor_PinRectBorder)
        .value("STYLE_COLOR_FLOW", ax::NodeEditor::StyleColor::StyleColor_Flow)
        .value("STYLE_COLOR_FLOW_MARKER", ax::NodeEditor::StyleColor::StyleColor_FlowMarker)
        .value("STYLE_COLOR_GROUP_BG", ax::NodeEditor::StyleColor::StyleColor_GroupBg)
        .value("STYLE_COLOR_GROUP_BORDER", ax::NodeEditor::StyleColor::StyleColor_GroupBorder)
        .value("STYLE_COLOR_COUNT", ax::NodeEditor::StyleColor::StyleColor_Count)
        .export_values();

    py::enum_<ax::NodeEditor::StyleVar>(libaimbp, "StyleVar", py::arithmetic())
        .value("STYLE_VAR_NODE_PADDING", ax::NodeEditor::StyleVar::StyleVar_NodePadding)
        .value("STYLE_VAR_NODE_ROUNDING", ax::NodeEditor::StyleVar::StyleVar_NodeRounding)
        .value("STYLE_VAR_NODE_BORDER_WIDTH", ax::NodeEditor::StyleVar::StyleVar_NodeBorderWidth)
        .value("STYLE_VAR_HOVERED_NODE_BORDER_WIDTH", ax::NodeEditor::StyleVar::StyleVar_HoveredNodeBorderWidth)
        .value("STYLE_VAR_SELECTED_NODE_BORDER_WIDTH", ax::NodeEditor::StyleVar::StyleVar_SelectedNodeBorderWidth)
        .value("STYLE_VAR_PIN_ROUNDING", ax::NodeEditor::StyleVar::StyleVar_PinRounding)
        .value("STYLE_VAR_PIN_BORDER_WIDTH", ax::NodeEditor::StyleVar::StyleVar_PinBorderWidth)
        .value("STYLE_VAR_LINK_STRENGTH", ax::NodeEditor::StyleVar::StyleVar_LinkStrength)
        .value("STYLE_VAR_SOURCE_DIRECTION", ax::NodeEditor::StyleVar::StyleVar_SourceDirection)
        .value("STYLE_VAR_TARGET_DIRECTION", ax::NodeEditor::StyleVar::StyleVar_TargetDirection)
        .value("STYLE_VAR_SCROLL_DURATION", ax::NodeEditor::StyleVar::StyleVar_ScrollDuration)
        .value("STYLE_VAR_FLOW_MARKER_DISTANCE", ax::NodeEditor::StyleVar::StyleVar_FlowMarkerDistance)
        .value("STYLE_VAR_FLOW_SPEED", ax::NodeEditor::StyleVar::StyleVar_FlowSpeed)
        .value("STYLE_VAR_FLOW_DURATION", ax::NodeEditor::StyleVar::StyleVar_FlowDuration)
        .value("STYLE_VAR_PIVOT_ALIGNMENT", ax::NodeEditor::StyleVar::StyleVar_PivotAlignment)
        .value("STYLE_VAR_PIVOT_SIZE", ax::NodeEditor::StyleVar::StyleVar_PivotSize)
        .value("STYLE_VAR_PIVOT_SCALE", ax::NodeEditor::StyleVar::StyleVar_PivotScale)
        .value("STYLE_VAR_PIN_CORNERS", ax::NodeEditor::StyleVar::StyleVar_PinCorners)
        .value("STYLE_VAR_PIN_RADIUS", ax::NodeEditor::StyleVar::StyleVar_PinRadius)
        .value("STYLE_VAR_PIN_ARROW_SIZE", ax::NodeEditor::StyleVar::StyleVar_PinArrowSize)
        .value("STYLE_VAR_PIN_ARROW_WIDTH", ax::NodeEditor::StyleVar::StyleVar_PinArrowWidth)
        .value("STYLE_VAR_GROUP_ROUNDING", ax::NodeEditor::StyleVar::StyleVar_GroupRounding)
        .value("STYLE_VAR_GROUP_BORDER_WIDTH", ax::NodeEditor::StyleVar::StyleVar_GroupBorderWidth)
        .value("STYLE_VAR_COUNT", ax::NodeEditor::StyleVar::StyleVar_Count)
        .export_values();

    PYCLASS_BEGIN(libaimbp, ax::NodeEditor::Style, Style)
    Style.def_readwrite("node_padding", &ax::NodeEditor::Style::NodePadding);
    Style.def_readwrite("node_rounding", &ax::NodeEditor::Style::NodeRounding);
    Style.def_readwrite("node_border_width", &ax::NodeEditor::Style::NodeBorderWidth);
    Style.def_readwrite("hovered_node_border_width", &ax::NodeEditor::Style::HoveredNodeBorderWidth);
    Style.def_readwrite("selected_node_border_width", &ax::NodeEditor::Style::SelectedNodeBorderWidth);
    Style.def_readwrite("pin_rounding", &ax::NodeEditor::Style::PinRounding);
    Style.def_readwrite("pin_border_width", &ax::NodeEditor::Style::PinBorderWidth);
    Style.def_readwrite("link_strength", &ax::NodeEditor::Style::LinkStrength);
    Style.def_readwrite("source_direction", &ax::NodeEditor::Style::SourceDirection);
    Style.def_readwrite("target_direction", &ax::NodeEditor::Style::TargetDirection);
    Style.def_readwrite("scroll_duration", &ax::NodeEditor::Style::ScrollDuration);
    Style.def_readwrite("flow_marker_distance", &ax::NodeEditor::Style::FlowMarkerDistance);
    Style.def_readwrite("flow_speed", &ax::NodeEditor::Style::FlowSpeed);
    Style.def_readwrite("flow_duration", &ax::NodeEditor::Style::FlowDuration);
    Style.def_readwrite("pivot_alignment", &ax::NodeEditor::Style::PivotAlignment);
    Style.def_readwrite("pivot_size", &ax::NodeEditor::Style::PivotSize);
    Style.def_readwrite("pivot_scale", &ax::NodeEditor::Style::PivotScale);
    Style.def_readwrite("pin_corners", &ax::NodeEditor::Style::PinCorners);
    Style.def_readwrite("pin_radius", &ax::NodeEditor::Style::PinRadius);
    Style.def_readwrite("pin_arrow_size", &ax::NodeEditor::Style::PinArrowSize);
    Style.def_readwrite("pin_arrow_width", &ax::NodeEditor::Style::PinArrowWidth);
    Style.def_readwrite("group_rounding", &ax::NodeEditor::Style::GroupRounding);
    Style.def_readwrite("group_border_width", &ax::NodeEditor::Style::GroupBorderWidth);
    Style.def_readonly("colors", &ax::NodeEditor::Style::Colors);
    Style.def(py::init<>());
    PYCLASS_END(libaimbp, ax::NodeEditor::Style, Style)

    libaimbp.def("get_style", &ax::NodeEditor::GetStyle
    , py::return_value_policy::reference);
    libaimbp.def("get_style_color_name", &ax::NodeEditor::GetStyleColorName
    , py::arg("color_index")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("push_style_color", &ax::NodeEditor::PushStyleColor
    , py::arg("color_index")
    , py::arg("color")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pop_style_color", &ax::NodeEditor::PopStyleColor
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    libaimbp.def("push_style_var", py::overload_cast<ax::NodeEditor::StyleVar, float>(&ax::NodeEditor::PushStyleVar)
    , py::arg("var_index")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("push_style_var", py::overload_cast<ax::NodeEditor::StyleVar, const ImVec2 &>(&ax::NodeEditor::PushStyleVar)
    , py::arg("var_index")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("push_style_var", py::overload_cast<ax::NodeEditor::StyleVar, const ImVec4 &>(&ax::NodeEditor::PushStyleVar)
    , py::arg("var_index")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pop_style_var", &ax::NodeEditor::PopStyleVar
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin", &ax::NodeEditor::Begin
    , py::arg("id")
    , py::arg("size") = ImVec2(0,0)
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end", &ax::NodeEditor::End
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_node", &ax::NodeEditor::BeginNode
    , py::arg("id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_pin", &ax::NodeEditor::BeginPin
    , py::arg("id")
    , py::arg("kind")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_rect", &ax::NodeEditor::PinRect
    , py::arg("a")
    , py::arg("b")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_pivot_rect", &ax::NodeEditor::PinPivotRect
    , py::arg("a")
    , py::arg("b")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_pivot_size", &ax::NodeEditor::PinPivotSize
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_pivot_scale", &ax::NodeEditor::PinPivotScale
    , py::arg("scale")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_pivot_alignment", &ax::NodeEditor::PinPivotAlignment
    , py::arg("alignment")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_pin", &ax::NodeEditor::EndPin
    , py::return_value_policy::automatic_reference);
    libaimbp.def("group", &ax::NodeEditor::Group
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_node", &ax::NodeEditor::EndNode
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_group_hint", &ax::NodeEditor::BeginGroupHint
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_group_min", &ax::NodeEditor::GetGroupMin
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_group_max", &ax::NodeEditor::GetGroupMax
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_hint_foreground_draw_list", &ax::NodeEditor::GetHintForegroundDrawList
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_hint_background_draw_list", &ax::NodeEditor::GetHintBackgroundDrawList
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_group_hint", &ax::NodeEditor::EndGroupHint
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_node_background_draw_list", &ax::NodeEditor::GetNodeBackgroundDrawList
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("link", &ax::NodeEditor::Link
    , py::arg("id")
    , py::arg("start_pin_id")
    , py::arg("end_pin_id")
    , py::arg("color") = ImVec4(1,1,1,1)
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    libaimbp.def("flow", &ax::NodeEditor::Flow
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_create", &ax::NodeEditor::BeginCreate
    , py::arg("color") = ImVec4(1,1,1,1)
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    libaimbp.def("query_new_node", py::overload_cast<ax::NodeEditor::PinId *>(&ax::NodeEditor::QueryNewNode)
    , py::arg("pin_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("query_new_node", py::overload_cast<ax::NodeEditor::PinId *, const ImVec4 &, float>(&ax::NodeEditor::QueryNewNode)
    , py::arg("pin_id")
    , py::arg("color")
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_new_item", py::overload_cast<>(&ax::NodeEditor::AcceptNewItem)
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_new_item", py::overload_cast<const ImVec4 &, float>(&ax::NodeEditor::AcceptNewItem)
    , py::arg("color")
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    libaimbp.def("reject_new_item", py::overload_cast<>(&ax::NodeEditor::RejectNewItem)
    , py::return_value_policy::automatic_reference);
    libaimbp.def("reject_new_item", py::overload_cast<const ImVec4 &, float>(&ax::NodeEditor::RejectNewItem)
    , py::arg("color")
    , py::arg("thickness") = 1.0f
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_create", &ax::NodeEditor::EndCreate
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_delete", &ax::NodeEditor::BeginDelete
    , py::return_value_policy::automatic_reference);
    libaimbp.def("query_deleted_link", &ax::NodeEditor::QueryDeletedLink
    , py::arg("link_id")
    , py::arg("start_id") = nullptr
    , py::arg("end_id") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimbp.def("query_deleted_node", &ax::NodeEditor::QueryDeletedNode
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_deleted_item", &ax::NodeEditor::AcceptDeletedItem
    , py::return_value_policy::automatic_reference);
    libaimbp.def("reject_deleted_item", &ax::NodeEditor::RejectDeletedItem
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_delete", &ax::NodeEditor::EndDelete
    , py::return_value_policy::automatic_reference);
    libaimbp.def("set_node_position", &ax::NodeEditor::SetNodePosition
    , py::arg("node_id")
    , py::arg("editor_position")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_node_position", &ax::NodeEditor::GetNodePosition
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_node_size", &ax::NodeEditor::GetNodeSize
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("center_node_on_screen", &ax::NodeEditor::CenterNodeOnScreen
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("restore_node_state", &ax::NodeEditor::RestoreNodeState
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("suspend", &ax::NodeEditor::Suspend
    , py::return_value_policy::automatic_reference);
    libaimbp.def("resume", &ax::NodeEditor::Resume
    , py::return_value_policy::automatic_reference);
    libaimbp.def("is_suspended", &ax::NodeEditor::IsSuspended
    , py::return_value_policy::automatic_reference);
    libaimbp.def("is_active", &ax::NodeEditor::IsActive
    , py::return_value_policy::automatic_reference);
    libaimbp.def("has_selection_changed", &ax::NodeEditor::HasSelectionChanged
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_selected_object_count", &ax::NodeEditor::GetSelectedObjectCount
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_selected_nodes", &ax::NodeEditor::GetSelectedNodes
    , py::arg("nodes")
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_selected_links", &ax::NodeEditor::GetSelectedLinks
    , py::arg("links")
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("clear_selection", &ax::NodeEditor::ClearSelection
    , py::return_value_policy::automatic_reference);
    libaimbp.def("select_node", &ax::NodeEditor::SelectNode
    , py::arg("node_id")
    , py::arg("append") = false
    , py::return_value_policy::automatic_reference);
    libaimbp.def("select_link", &ax::NodeEditor::SelectLink
    , py::arg("link_id")
    , py::arg("append") = false
    , py::return_value_policy::automatic_reference);
    libaimbp.def("deselect_node", &ax::NodeEditor::DeselectNode
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("deselect_link", &ax::NodeEditor::DeselectLink
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("delete_node", &ax::NodeEditor::DeleteNode
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("delete_link", &ax::NodeEditor::DeleteLink
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("navigate_to_content", &ax::NodeEditor::NavigateToContent
    , py::arg("duration") = -1
    , py::return_value_policy::automatic_reference);
    libaimbp.def("navigate_to_selection", &ax::NodeEditor::NavigateToSelection
    , py::arg("zoom_in") = false
    , py::arg("duration") = -1
    , py::return_value_policy::automatic_reference);
    libaimbp.def("show_node_context_menu", &ax::NodeEditor::ShowNodeContextMenu
    , py::arg("node_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("show_pin_context_menu", &ax::NodeEditor::ShowPinContextMenu
    , py::arg("pin_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("show_link_context_menu", &ax::NodeEditor::ShowLinkContextMenu
    , py::arg("link_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("show_background_context_menu", &ax::NodeEditor::ShowBackgroundContextMenu
    , py::return_value_policy::automatic_reference);
    libaimbp.def("enable_shortcuts", &ax::NodeEditor::EnableShortcuts
    , py::arg("enable")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("are_shortcuts_enabled", &ax::NodeEditor::AreShortcutsEnabled
    , py::return_value_policy::automatic_reference);
    libaimbp.def("begin_shortcut", &ax::NodeEditor::BeginShortcut
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_cut", &ax::NodeEditor::AcceptCut
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_copy", &ax::NodeEditor::AcceptCopy
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_paste", &ax::NodeEditor::AcceptPaste
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_duplicate", &ax::NodeEditor::AcceptDuplicate
    , py::return_value_policy::automatic_reference);
    libaimbp.def("accept_create_node", &ax::NodeEditor::AcceptCreateNode
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_action_context_size", &ax::NodeEditor::GetActionContextSize
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_action_context_nodes", &ax::NodeEditor::GetActionContextNodes
    , py::arg("nodes")
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_action_context_links", &ax::NodeEditor::GetActionContextLinks
    , py::arg("links")
    , py::arg("size")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("end_shortcut", &ax::NodeEditor::EndShortcut
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_current_zoom", &ax::NodeEditor::GetCurrentZoom
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_double_clicked_node", &ax::NodeEditor::GetDoubleClickedNode
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_double_clicked_pin", &ax::NodeEditor::GetDoubleClickedPin
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_double_clicked_link", &ax::NodeEditor::GetDoubleClickedLink
    , py::return_value_policy::automatic_reference);
    libaimbp.def("is_background_clicked", &ax::NodeEditor::IsBackgroundClicked
    , py::return_value_policy::automatic_reference);
    libaimbp.def("is_background_double_clicked", &ax::NodeEditor::IsBackgroundDoubleClicked
    , py::return_value_policy::automatic_reference);
    libaimbp.def("pin_had_any_links", &ax::NodeEditor::PinHadAnyLinks
    , py::arg("pin_id")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("get_screen_size", &ax::NodeEditor::GetScreenSize
    , py::return_value_policy::automatic_reference);
    libaimbp.def("screen_to_canvas", &ax::NodeEditor::ScreenToCanvas
    , py::arg("pos")
    , py::return_value_policy::automatic_reference);
    libaimbp.def("canvas_to_screen", &ax::NodeEditor::CanvasToScreen
    , py::arg("pos")
    , py::return_value_policy::automatic_reference);
    PYCLASS_BEGIN(libaimbp, ax::NodeEditor::NodeId, NodeId)
    PYCLASS_END(libaimbp, ax::NodeEditor::NodeId, NodeId)

    PYCLASS_BEGIN(libaimbp, ax::NodeEditor::LinkId, LinkId)
    PYCLASS_END(libaimbp, ax::NodeEditor::LinkId, LinkId)

    PYCLASS_BEGIN(libaimbp, ax::NodeEditor::PinId, PinId)
    PYCLASS_END(libaimbp, ax::NodeEditor::PinId, PinId)


}

