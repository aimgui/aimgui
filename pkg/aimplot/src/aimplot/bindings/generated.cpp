#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include "implot.h"
#include "implot_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_generated(py::module &_aimplot, Registry &registry) {
    py::enum_<ImAxis_>(_aimplot, "Axis", py::arithmetic())
        .value("AXIS_X1", ImAxis_X1)
        .value("AXIS_X2", ImAxis_X2)
        .value("AXIS_X3", ImAxis_X3)
        .value("AXIS_Y1", ImAxis_Y1)
        .value("AXIS_Y2", ImAxis_Y2)
        .value("AXIS_Y3", ImAxis_Y3)
        .value("AXIS_COUNT", ImAxis_COUNT)
        .export_values();

    py::enum_<ImPlotFlags_>(_aimplot, "Flags", py::arithmetic())
        .value("FLAGS_NONE", ImPlotFlags_None)
        .value("FLAGS_NO_TITLE", ImPlotFlags_NoTitle)
        .value("FLAGS_NO_LEGEND", ImPlotFlags_NoLegend)
        .value("FLAGS_NO_MOUSE_TEXT", ImPlotFlags_NoMouseText)
        .value("FLAGS_NO_INPUTS", ImPlotFlags_NoInputs)
        .value("FLAGS_NO_MENUS", ImPlotFlags_NoMenus)
        .value("FLAGS_NO_BOX_SELECT", ImPlotFlags_NoBoxSelect)
        .value("FLAGS_NO_CHILD", ImPlotFlags_NoChild)
        .value("FLAGS_NO_FRAME", ImPlotFlags_NoFrame)
        .value("FLAGS_EQUAL", ImPlotFlags_Equal)
        .value("FLAGS_CROSSHAIRS", ImPlotFlags_Crosshairs)
        .value("FLAGS_CANVAS_ONLY", ImPlotFlags_CanvasOnly)
        .export_values();

    py::enum_<ImPlotAxisFlags_>(_aimplot, "AxisFlags", py::arithmetic())
        .value("AXIS_FLAGS_NONE", ImPlotAxisFlags_None)
        .value("AXIS_FLAGS_NO_LABEL", ImPlotAxisFlags_NoLabel)
        .value("AXIS_FLAGS_NO_GRID_LINES", ImPlotAxisFlags_NoGridLines)
        .value("AXIS_FLAGS_NO_TICK_MARKS", ImPlotAxisFlags_NoTickMarks)
        .value("AXIS_FLAGS_NO_TICK_LABELS", ImPlotAxisFlags_NoTickLabels)
        .value("AXIS_FLAGS_NO_INITIAL_FIT", ImPlotAxisFlags_NoInitialFit)
        .value("AXIS_FLAGS_NO_MENUS", ImPlotAxisFlags_NoMenus)
        .value("AXIS_FLAGS_NO_SIDE_SWITCH", ImPlotAxisFlags_NoSideSwitch)
        .value("AXIS_FLAGS_NO_HIGHLIGHT", ImPlotAxisFlags_NoHighlight)
        .value("AXIS_FLAGS_OPPOSITE", ImPlotAxisFlags_Opposite)
        .value("AXIS_FLAGS_FOREGROUND", ImPlotAxisFlags_Foreground)
        .value("AXIS_FLAGS_INVERT", ImPlotAxisFlags_Invert)
        .value("AXIS_FLAGS_AUTO_FIT", ImPlotAxisFlags_AutoFit)
        .value("AXIS_FLAGS_RANGE_FIT", ImPlotAxisFlags_RangeFit)
        .value("AXIS_FLAGS_PAN_STRETCH", ImPlotAxisFlags_PanStretch)
        .value("AXIS_FLAGS_LOCK_MIN", ImPlotAxisFlags_LockMin)
        .value("AXIS_FLAGS_LOCK_MAX", ImPlotAxisFlags_LockMax)
        .value("AXIS_FLAGS_LOCK", ImPlotAxisFlags_Lock)
        .value("AXIS_FLAGS_NO_DECORATIONS", ImPlotAxisFlags_NoDecorations)
        .value("AXIS_FLAGS_AUX_DEFAULT", ImPlotAxisFlags_AuxDefault)
        .export_values();

    py::enum_<ImPlotSubplotFlags_>(_aimplot, "SubplotFlags", py::arithmetic())
        .value("SUBPLOT_FLAGS_NONE", ImPlotSubplotFlags_None)
        .value("SUBPLOT_FLAGS_NO_TITLE", ImPlotSubplotFlags_NoTitle)
        .value("SUBPLOT_FLAGS_NO_LEGEND", ImPlotSubplotFlags_NoLegend)
        .value("SUBPLOT_FLAGS_NO_MENUS", ImPlotSubplotFlags_NoMenus)
        .value("SUBPLOT_FLAGS_NO_RESIZE", ImPlotSubplotFlags_NoResize)
        .value("SUBPLOT_FLAGS_NO_ALIGN", ImPlotSubplotFlags_NoAlign)
        .value("SUBPLOT_FLAGS_SHARE_ITEMS", ImPlotSubplotFlags_ShareItems)
        .value("SUBPLOT_FLAGS_LINK_ROWS", ImPlotSubplotFlags_LinkRows)
        .value("SUBPLOT_FLAGS_LINK_COLS", ImPlotSubplotFlags_LinkCols)
        .value("SUBPLOT_FLAGS_LINK_ALL_X", ImPlotSubplotFlags_LinkAllX)
        .value("SUBPLOT_FLAGS_LINK_ALL_Y", ImPlotSubplotFlags_LinkAllY)
        .value("SUBPLOT_FLAGS_COL_MAJOR", ImPlotSubplotFlags_ColMajor)
        .export_values();

    py::enum_<ImPlotLegendFlags_>(_aimplot, "LegendFlags", py::arithmetic())
        .value("LEGEND_FLAGS_NONE", ImPlotLegendFlags_None)
        .value("LEGEND_FLAGS_NO_BUTTONS", ImPlotLegendFlags_NoButtons)
        .value("LEGEND_FLAGS_NO_HIGHLIGHT_ITEM", ImPlotLegendFlags_NoHighlightItem)
        .value("LEGEND_FLAGS_NO_HIGHLIGHT_AXIS", ImPlotLegendFlags_NoHighlightAxis)
        .value("LEGEND_FLAGS_NO_MENUS", ImPlotLegendFlags_NoMenus)
        .value("LEGEND_FLAGS_OUTSIDE", ImPlotLegendFlags_Outside)
        .value("LEGEND_FLAGS_HORIZONTAL", ImPlotLegendFlags_Horizontal)
        .value("LEGEND_FLAGS_SORT", ImPlotLegendFlags_Sort)
        .export_values();

    py::enum_<ImPlotMouseTextFlags_>(_aimplot, "MouseTextFlags", py::arithmetic())
        .value("MOUSE_TEXT_FLAGS_NONE", ImPlotMouseTextFlags_None)
        .value("MOUSE_TEXT_FLAGS_NO_AUX_AXES", ImPlotMouseTextFlags_NoAuxAxes)
        .value("MOUSE_TEXT_FLAGS_NO_FORMAT", ImPlotMouseTextFlags_NoFormat)
        .value("MOUSE_TEXT_FLAGS_SHOW_ALWAYS", ImPlotMouseTextFlags_ShowAlways)
        .export_values();

    py::enum_<ImPlotDragToolFlags_>(_aimplot, "DragToolFlags", py::arithmetic())
        .value("DRAG_TOOL_FLAGS_NONE", ImPlotDragToolFlags_None)
        .value("DRAG_TOOL_FLAGS_NO_CURSORS", ImPlotDragToolFlags_NoCursors)
        .value("DRAG_TOOL_FLAGS_NO_FIT", ImPlotDragToolFlags_NoFit)
        .value("DRAG_TOOL_FLAGS_NO_INPUTS", ImPlotDragToolFlags_NoInputs)
        .value("DRAG_TOOL_FLAGS_DELAYED", ImPlotDragToolFlags_Delayed)
        .export_values();

    py::enum_<ImPlotColormapScaleFlags_>(_aimplot, "ColormapScaleFlags", py::arithmetic())
        .value("COLORMAP_SCALE_FLAGS_NONE", ImPlotColormapScaleFlags_None)
        .value("COLORMAP_SCALE_FLAGS_NO_LABEL", ImPlotColormapScaleFlags_NoLabel)
        .value("COLORMAP_SCALE_FLAGS_OPPOSITE", ImPlotColormapScaleFlags_Opposite)
        .value("COLORMAP_SCALE_FLAGS_INVERT", ImPlotColormapScaleFlags_Invert)
        .export_values();

    py::enum_<ImPlotItemFlags_>(_aimplot, "ItemFlags", py::arithmetic())
        .value("ITEM_FLAGS_NONE", ImPlotItemFlags_None)
        .value("ITEM_FLAGS_NO_LEGEND", ImPlotItemFlags_NoLegend)
        .value("ITEM_FLAGS_NO_FIT", ImPlotItemFlags_NoFit)
        .export_values();

    py::enum_<ImPlotLineFlags_>(_aimplot, "LineFlags", py::arithmetic())
        .value("LINE_FLAGS_NONE", ImPlotLineFlags_None)
        .value("LINE_FLAGS_SEGMENTS", ImPlotLineFlags_Segments)
        .value("LINE_FLAGS_LOOP", ImPlotLineFlags_Loop)
        .value("LINE_FLAGS_SKIP_NA_N", ImPlotLineFlags_SkipNaN)
        .value("LINE_FLAGS_NO_CLIP", ImPlotLineFlags_NoClip)
        .value("LINE_FLAGS_SHADED", ImPlotLineFlags_Shaded)
        .export_values();

    py::enum_<ImPlotScatterFlags_>(_aimplot, "ScatterFlags", py::arithmetic())
        .value("SCATTER_FLAGS_NONE", ImPlotScatterFlags_None)
        .value("SCATTER_FLAGS_NO_CLIP", ImPlotScatterFlags_NoClip)
        .export_values();

    py::enum_<ImPlotStairsFlags_>(_aimplot, "StairsFlags", py::arithmetic())
        .value("STAIRS_FLAGS_NONE", ImPlotStairsFlags_None)
        .value("STAIRS_FLAGS_PRE_STEP", ImPlotStairsFlags_PreStep)
        .value("STAIRS_FLAGS_SHADED", ImPlotStairsFlags_Shaded)
        .export_values();

    py::enum_<ImPlotShadedFlags_>(_aimplot, "ShadedFlags", py::arithmetic())
        .value("SHADED_FLAGS_NONE", ImPlotShadedFlags_None)
        .export_values();

    py::enum_<ImPlotBarsFlags_>(_aimplot, "BarsFlags", py::arithmetic())
        .value("BARS_FLAGS_NONE", ImPlotBarsFlags_None)
        .value("BARS_FLAGS_HORIZONTAL", ImPlotBarsFlags_Horizontal)
        .export_values();

    py::enum_<ImPlotBarGroupsFlags_>(_aimplot, "BarGroupsFlags", py::arithmetic())
        .value("BAR_GROUPS_FLAGS_NONE", ImPlotBarGroupsFlags_None)
        .value("BAR_GROUPS_FLAGS_HORIZONTAL", ImPlotBarGroupsFlags_Horizontal)
        .value("BAR_GROUPS_FLAGS_STACKED", ImPlotBarGroupsFlags_Stacked)
        .export_values();

    py::enum_<ImPlotErrorBarsFlags_>(_aimplot, "ErrorBarsFlags", py::arithmetic())
        .value("ERROR_BARS_FLAGS_NONE", ImPlotErrorBarsFlags_None)
        .value("ERROR_BARS_FLAGS_HORIZONTAL", ImPlotErrorBarsFlags_Horizontal)
        .export_values();

    py::enum_<ImPlotStemsFlags_>(_aimplot, "StemsFlags", py::arithmetic())
        .value("STEMS_FLAGS_NONE", ImPlotStemsFlags_None)
        .value("STEMS_FLAGS_HORIZONTAL", ImPlotStemsFlags_Horizontal)
        .export_values();

    py::enum_<ImPlotInfLinesFlags_>(_aimplot, "InfLinesFlags", py::arithmetic())
        .value("INF_LINES_FLAGS_NONE", ImPlotInfLinesFlags_None)
        .value("INF_LINES_FLAGS_HORIZONTAL", ImPlotInfLinesFlags_Horizontal)
        .export_values();

    py::enum_<ImPlotPieChartFlags_>(_aimplot, "PieChartFlags", py::arithmetic())
        .value("PIE_CHART_FLAGS_NONE", ImPlotPieChartFlags_None)
        .value("PIE_CHART_FLAGS_NORMALIZE", ImPlotPieChartFlags_Normalize)
        .export_values();

    py::enum_<ImPlotHeatmapFlags_>(_aimplot, "HeatmapFlags", py::arithmetic())
        .value("HEATMAP_FLAGS_NONE", ImPlotHeatmapFlags_None)
        .value("HEATMAP_FLAGS_COL_MAJOR", ImPlotHeatmapFlags_ColMajor)
        .export_values();

    py::enum_<ImPlotHistogramFlags_>(_aimplot, "HistogramFlags", py::arithmetic())
        .value("HISTOGRAM_FLAGS_NONE", ImPlotHistogramFlags_None)
        .value("HISTOGRAM_FLAGS_HORIZONTAL", ImPlotHistogramFlags_Horizontal)
        .value("HISTOGRAM_FLAGS_CUMULATIVE", ImPlotHistogramFlags_Cumulative)
        .value("HISTOGRAM_FLAGS_DENSITY", ImPlotHistogramFlags_Density)
        .value("HISTOGRAM_FLAGS_NO_OUTLIERS", ImPlotHistogramFlags_NoOutliers)
        .value("HISTOGRAM_FLAGS_COL_MAJOR", ImPlotHistogramFlags_ColMajor)
        .export_values();

    py::enum_<ImPlotDigitalFlags_>(_aimplot, "DigitalFlags", py::arithmetic())
        .value("DIGITAL_FLAGS_NONE", ImPlotDigitalFlags_None)
        .export_values();

    py::enum_<ImPlotImageFlags_>(_aimplot, "ageFlags", py::arithmetic())
        .value("AGE_FLAGS_NONE", ImPlotImageFlags_None)
        .export_values();

    py::enum_<ImPlotTextFlags_>(_aimplot, "TextFlags", py::arithmetic())
        .value("TEXT_FLAGS_NONE", ImPlotTextFlags_None)
        .value("TEXT_FLAGS_VERTICAL", ImPlotTextFlags_Vertical)
        .export_values();

    py::enum_<ImPlotDummyFlags_>(_aimplot, "DummyFlags", py::arithmetic())
        .value("DUMMY_FLAGS_NONE", ImPlotDummyFlags_None)
        .export_values();

    py::enum_<ImPlotCond_>(_aimplot, "Cond", py::arithmetic())
        .value("COND_NONE", ImPlotCond_None)
        .value("COND_ALWAYS", ImPlotCond_Always)
        .value("COND_ONCE", ImPlotCond_Once)
        .export_values();

    py::enum_<ImPlotCol_>(_aimplot, "Col", py::arithmetic())
        .value("COL_LINE", ImPlotCol_Line)
        .value("COL_FILL", ImPlotCol_Fill)
        .value("COL_MARKER_OUTLINE", ImPlotCol_MarkerOutline)
        .value("COL_MARKER_FILL", ImPlotCol_MarkerFill)
        .value("COL_ERROR_BAR", ImPlotCol_ErrorBar)
        .value("COL_FRAME_BG", ImPlotCol_FrameBg)
        .value("COL_PLOT_BG", ImPlotCol_PlotBg)
        .value("COL_PLOT_BORDER", ImPlotCol_PlotBorder)
        .value("COL_LEGEND_BG", ImPlotCol_LegendBg)
        .value("COL_LEGEND_BORDER", ImPlotCol_LegendBorder)
        .value("COL_LEGEND_TEXT", ImPlotCol_LegendText)
        .value("COL_TITLE_TEXT", ImPlotCol_TitleText)
        .value("COL_INLAY_TEXT", ImPlotCol_InlayText)
        .value("COL_AXIS_TEXT", ImPlotCol_AxisText)
        .value("COL_AXIS_GRID", ImPlotCol_AxisGrid)
        .value("COL_AXIS_TICK", ImPlotCol_AxisTick)
        .value("COL_AXIS_BG", ImPlotCol_AxisBg)
        .value("COL_AXIS_BG_HOVERED", ImPlotCol_AxisBgHovered)
        .value("COL_AXIS_BG_ACTIVE", ImPlotCol_AxisBgActive)
        .value("COL_SELECTION", ImPlotCol_Selection)
        .value("COL_CROSSHAIRS", ImPlotCol_Crosshairs)
        .value("COL_COUNT", ImPlotCol_COUNT)
        .export_values();

    py::enum_<ImPlotStyleVar_>(_aimplot, "StyleVar", py::arithmetic())
        .value("STYLE_VAR_LINE_WEIGHT", ImPlotStyleVar_LineWeight)
        .value("STYLE_VAR_MARKER", ImPlotStyleVar_Marker)
        .value("STYLE_VAR_MARKER_SIZE", ImPlotStyleVar_MarkerSize)
        .value("STYLE_VAR_MARKER_WEIGHT", ImPlotStyleVar_MarkerWeight)
        .value("STYLE_VAR_FILL_ALPHA", ImPlotStyleVar_FillAlpha)
        .value("STYLE_VAR_ERROR_BAR_SIZE", ImPlotStyleVar_ErrorBarSize)
        .value("STYLE_VAR_ERROR_BAR_WEIGHT", ImPlotStyleVar_ErrorBarWeight)
        .value("STYLE_VAR_DIGITAL_BIT_HEIGHT", ImPlotStyleVar_DigitalBitHeight)
        .value("STYLE_VAR_DIGITAL_BIT_GAP", ImPlotStyleVar_DigitalBitGap)
        .value("STYLE_VAR_PLOT_BORDER_SIZE", ImPlotStyleVar_PlotBorderSize)
        .value("STYLE_VAR_MINOR_ALPHA", ImPlotStyleVar_MinorAlpha)
        .value("STYLE_VAR_MAJOR_TICK_LEN", ImPlotStyleVar_MajorTickLen)
        .value("STYLE_VAR_MINOR_TICK_LEN", ImPlotStyleVar_MinorTickLen)
        .value("STYLE_VAR_MAJOR_TICK_SIZE", ImPlotStyleVar_MajorTickSize)
        .value("STYLE_VAR_MINOR_TICK_SIZE", ImPlotStyleVar_MinorTickSize)
        .value("STYLE_VAR_MAJOR_GRID_SIZE", ImPlotStyleVar_MajorGridSize)
        .value("STYLE_VAR_MINOR_GRID_SIZE", ImPlotStyleVar_MinorGridSize)
        .value("STYLE_VAR_PLOT_PADDING", ImPlotStyleVar_PlotPadding)
        .value("STYLE_VAR_LABEL_PADDING", ImPlotStyleVar_LabelPadding)
        .value("STYLE_VAR_LEGEND_PADDING", ImPlotStyleVar_LegendPadding)
        .value("STYLE_VAR_LEGEND_INNER_PADDING", ImPlotStyleVar_LegendInnerPadding)
        .value("STYLE_VAR_LEGEND_SPACING", ImPlotStyleVar_LegendSpacing)
        .value("STYLE_VAR_MOUSE_POS_PADDING", ImPlotStyleVar_MousePosPadding)
        .value("STYLE_VAR_ANNOTATION_PADDING", ImPlotStyleVar_AnnotationPadding)
        .value("STYLE_VAR_FIT_PADDING", ImPlotStyleVar_FitPadding)
        .value("STYLE_VAR_PLOT_DEFAULT_SIZE", ImPlotStyleVar_PlotDefaultSize)
        .value("STYLE_VAR_PLOT_MIN_SIZE", ImPlotStyleVar_PlotMinSize)
        .value("STYLE_VAR_COUNT", ImPlotStyleVar_COUNT)
        .export_values();

    py::enum_<ImPlotScale_>(_aimplot, "Scale", py::arithmetic())
        .value("SCALE_LINEAR", ImPlotScale_Linear)
        .value("SCALE_TIME", ImPlotScale_Time)
        .value("SCALE_LOG10", ImPlotScale_Log10)
        .value("SCALE_SYM_LOG", ImPlotScale_SymLog)
        .export_values();

    py::enum_<ImPlotMarker_>(_aimplot, "Marker", py::arithmetic())
        .value("MARKER_NONE", ImPlotMarker_None)
        .value("MARKER_CIRCLE", ImPlotMarker_Circle)
        .value("MARKER_SQUARE", ImPlotMarker_Square)
        .value("MARKER_DIAMOND", ImPlotMarker_Diamond)
        .value("MARKER_UP", ImPlotMarker_Up)
        .value("MARKER_DOWN", ImPlotMarker_Down)
        .value("MARKER_LEFT", ImPlotMarker_Left)
        .value("MARKER_RIGHT", ImPlotMarker_Right)
        .value("MARKER_CROSS", ImPlotMarker_Cross)
        .value("MARKER_PLUS", ImPlotMarker_Plus)
        .value("MARKER_ASTERISK", ImPlotMarker_Asterisk)
        .value("MARKER_COUNT", ImPlotMarker_COUNT)
        .export_values();

    py::enum_<ImPlotColormap_>(_aimplot, "Colormap", py::arithmetic())
        .value("COLORMAP_DEEP", ImPlotColormap_Deep)
        .value("COLORMAP_DARK", ImPlotColormap_Dark)
        .value("COLORMAP_PASTEL", ImPlotColormap_Pastel)
        .value("COLORMAP_PAIRED", ImPlotColormap_Paired)
        .value("COLORMAP_VIRIDIS", ImPlotColormap_Viridis)
        .value("COLORMAP_PLASMA", ImPlotColormap_Plasma)
        .value("COLORMAP_HOT", ImPlotColormap_Hot)
        .value("COLORMAP_COOL", ImPlotColormap_Cool)
        .value("COLORMAP_PINK", ImPlotColormap_Pink)
        .value("COLORMAP_JET", ImPlotColormap_Jet)
        .value("COLORMAP_TWILIGHT", ImPlotColormap_Twilight)
        .value("COLORMAP_RD_BU", ImPlotColormap_RdBu)
        .value("COLORMAP_BR_BG", ImPlotColormap_BrBG)
        .value("COLORMAP_PI_YG", ImPlotColormap_PiYG)
        .value("COLORMAP_SPECTRAL", ImPlotColormap_Spectral)
        .value("COLORMAP_GREYS", ImPlotColormap_Greys)
        .export_values();

    py::enum_<ImPlotLocation_>(_aimplot, "Location", py::arithmetic())
        .value("LOCATION_CENTER", ImPlotLocation_Center)
        .value("LOCATION_NORTH", ImPlotLocation_North)
        .value("LOCATION_SOUTH", ImPlotLocation_South)
        .value("LOCATION_WEST", ImPlotLocation_West)
        .value("LOCATION_EAST", ImPlotLocation_East)
        .value("LOCATION_NORTH_WEST", ImPlotLocation_NorthWest)
        .value("LOCATION_NORTH_EAST", ImPlotLocation_NorthEast)
        .value("LOCATION_SOUTH_WEST", ImPlotLocation_SouthWest)
        .value("LOCATION_SOUTH_EAST", ImPlotLocation_SouthEast)
        .export_values();

    py::enum_<ImPlotBin_>(_aimplot, "Bin", py::arithmetic())
        .value("BIN_SQRT", ImPlotBin_Sqrt)
        .value("BIN_STURGES", ImPlotBin_Sturges)
        .value("BIN_RICE", ImPlotBin_Rice)
        .value("BIN_SCOTT", ImPlotBin_Scott)
        .export_values();

    PYCLASS_BEGIN(_aimplot, ImPlotPoint, Point)
    Point.def_readwrite("x", &ImPlotPoint::x);
    Point.def_readwrite("y", &ImPlotPoint::y);
    Point.def(py::init<>());
    Point.def(py::init<double, double>()
    , py::arg("_x")
    , py::arg("_y")
    );
    Point.def(py::init<const ImVec2 &>()
    , py::arg("p")
    );
    PYCLASS_END(_aimplot, ImPlotPoint, Point)

    PYCLASS_BEGIN(_aimplot, ImPlotRange, Range)
    Range.def_readwrite("min", &ImPlotRange::Min);
    Range.def_readwrite("max", &ImPlotRange::Max);
    Range.def(py::init<>());
    Range.def(py::init<double, double>()
    , py::arg("_min")
    , py::arg("_max")
    );
    Range.def("contains", &ImPlotRange::Contains
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    Range.def("size", &ImPlotRange::Size
    , py::return_value_policy::automatic_reference);
    Range.def("clamp", &ImPlotRange::Clamp
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    PYCLASS_END(_aimplot, ImPlotRange, Range)

    PYCLASS_BEGIN(_aimplot, ImPlotRect, Rect)
    Rect.def_readwrite("x", &ImPlotRect::X);
    Rect.def_readwrite("y", &ImPlotRect::Y);
    Rect.def(py::init<>());
    Rect.def(py::init<double, double, double, double>()
    , py::arg("x_min")
    , py::arg("x_max")
    , py::arg("y_min")
    , py::arg("y_max")
    );
    Rect.def("size", &ImPlotRect::Size
    , py::return_value_policy::automatic_reference);
    Rect.def("clamp", py::overload_cast<const ImPlotPoint &>(&ImPlotRect::Clamp)
    , py::arg("p")
    , py::return_value_policy::automatic_reference);
    Rect.def("clamp", py::overload_cast<double, double>(&ImPlotRect::Clamp)
    , py::arg("x")
    , py::arg("y")
    , py::return_value_policy::automatic_reference);
    Rect.def("min", &ImPlotRect::Min
    , py::return_value_policy::automatic_reference);
    Rect.def("max", &ImPlotRect::Max
    , py::return_value_policy::automatic_reference);
    PYCLASS_END(_aimplot, ImPlotRect, Rect)

    PYCLASS_BEGIN(_aimplot, ImPlotStyle, Style)
    Style.def_readwrite("line_weight", &ImPlotStyle::LineWeight);
    Style.def_readwrite("marker", &ImPlotStyle::Marker);
    Style.def_readwrite("marker_size", &ImPlotStyle::MarkerSize);
    Style.def_readwrite("marker_weight", &ImPlotStyle::MarkerWeight);
    Style.def_readwrite("fill_alpha", &ImPlotStyle::FillAlpha);
    Style.def_readwrite("error_bar_size", &ImPlotStyle::ErrorBarSize);
    Style.def_readwrite("error_bar_weight", &ImPlotStyle::ErrorBarWeight);
    Style.def_readwrite("digital_bit_height", &ImPlotStyle::DigitalBitHeight);
    Style.def_readwrite("digital_bit_gap", &ImPlotStyle::DigitalBitGap);
    Style.def_readwrite("plot_border_size", &ImPlotStyle::PlotBorderSize);
    Style.def_readwrite("minor_alpha", &ImPlotStyle::MinorAlpha);
    Style.def_readwrite("major_tick_len", &ImPlotStyle::MajorTickLen);
    Style.def_readwrite("minor_tick_len", &ImPlotStyle::MinorTickLen);
    Style.def_readwrite("major_tick_size", &ImPlotStyle::MajorTickSize);
    Style.def_readwrite("minor_tick_size", &ImPlotStyle::MinorTickSize);
    Style.def_readwrite("major_grid_size", &ImPlotStyle::MajorGridSize);
    Style.def_readwrite("minor_grid_size", &ImPlotStyle::MinorGridSize);
    Style.def_readwrite("plot_padding", &ImPlotStyle::PlotPadding);
    Style.def_readwrite("label_padding", &ImPlotStyle::LabelPadding);
    Style.def_readwrite("legend_padding", &ImPlotStyle::LegendPadding);
    Style.def_readwrite("legend_inner_padding", &ImPlotStyle::LegendInnerPadding);
    Style.def_readwrite("legend_spacing", &ImPlotStyle::LegendSpacing);
    Style.def_readwrite("mouse_pos_padding", &ImPlotStyle::MousePosPadding);
    Style.def_readwrite("annotation_padding", &ImPlotStyle::AnnotationPadding);
    Style.def_readwrite("fit_padding", &ImPlotStyle::FitPadding);
    Style.def_readwrite("plot_default_size", &ImPlotStyle::PlotDefaultSize);
    Style.def_readwrite("plot_min_size", &ImPlotStyle::PlotMinSize);
    Style.def_readonly("colors", &ImPlotStyle::Colors);
    Style.def_readwrite("colormap", &ImPlotStyle::Colormap);
    Style.def_readwrite("use_local_time", &ImPlotStyle::UseLocalTime);
    Style.def_readwrite("use_iso8601", &ImPlotStyle::UseISO8601);
    Style.def_readwrite("use24_hour_clock", &ImPlotStyle::Use24HourClock);
    Style.def(py::init<>());
    PYCLASS_END(_aimplot, ImPlotStyle, Style)

    PYCLASS_BEGIN(_aimplot, ImPlotInputMap, InputMap)
    InputMap.def_readwrite("pan", &ImPlotInputMap::Pan);
    InputMap.def_readwrite("pan_mod", &ImPlotInputMap::PanMod);
    InputMap.def_readwrite("fit", &ImPlotInputMap::Fit);
    InputMap.def_readwrite("select", &ImPlotInputMap::Select);
    InputMap.def_readwrite("select_cancel", &ImPlotInputMap::SelectCancel);
    InputMap.def_readwrite("select_mod", &ImPlotInputMap::SelectMod);
    InputMap.def_readwrite("select_horz_mod", &ImPlotInputMap::SelectHorzMod);
    InputMap.def_readwrite("select_vert_mod", &ImPlotInputMap::SelectVertMod);
    InputMap.def_readwrite("menu", &ImPlotInputMap::Menu);
    InputMap.def_readwrite("override_mod", &ImPlotInputMap::OverrideMod);
    InputMap.def_readwrite("zoom_mod", &ImPlotInputMap::ZoomMod);
    InputMap.def_readwrite("zoom_rate", &ImPlotInputMap::ZoomRate);
    InputMap.def(py::init<>());
    PYCLASS_END(_aimplot, ImPlotInputMap, InputMap)

    _aimplot.def("set_im_gui_context", &ImPlot::SetImGuiContext
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_plot", &ImPlot::BeginPlot
    , py::arg("title_id")
    , py::arg("size") = ImVec2(-1,0)
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_plot", &ImPlot::EndPlot
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_subplots", [](const char * title_id, int rows, int cols, const ImVec2 & size, ImPlotSubplotFlags flags, float * row_ratios, float * col_ratios)
    {
        auto ret = ImPlot::BeginSubplots(title_id, rows, cols, size, flags, row_ratios, col_ratios);
        return std::make_tuple(ret, row_ratios, col_ratios);
    }
    , py::arg("title_id")
    , py::arg("rows")
    , py::arg("cols")
    , py::arg("size")
    , py::arg("flags") = 0
    , py::arg("row_ratios") = nullptr
    , py::arg("col_ratios") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_subplots", &ImPlot::EndSubplots
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis", &ImPlot::SetupAxis
    , py::arg("axis")
    , py::arg("label") = nullptr
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_limits", &ImPlot::SetupAxisLimits
    , py::arg("axis")
    , py::arg("v_min")
    , py::arg("v_max")
    , py::arg("cond") = ImPlotCond_Once
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_links", [](ImAxis axis, double * link_min, double * link_max)
    {
        ImPlot::SetupAxisLinks(axis, link_min, link_max);
        return std::make_tuple(link_min, link_max);
    }
    , py::arg("axis")
    , py::arg("link_min")
    , py::arg("link_max")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_format", py::overload_cast<ImAxis, const char *>(&ImPlot::SetupAxisFormat)
    , py::arg("axis")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_scale", py::overload_cast<ImAxis, ImPlotScale>(&ImPlot::SetupAxisScale)
    , py::arg("axis")
    , py::arg("scale")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_limits_constraints", &ImPlot::SetupAxisLimitsConstraints
    , py::arg("axis")
    , py::arg("v_min")
    , py::arg("v_max")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axis_zoom_constraints", &ImPlot::SetupAxisZoomConstraints
    , py::arg("axis")
    , py::arg("z_min")
    , py::arg("z_max")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axes", &ImPlot::SetupAxes
    , py::arg("x_label")
    , py::arg("y_label")
    , py::arg("x_flags") = 0
    , py::arg("y_flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_axes_limits", &ImPlot::SetupAxesLimits
    , py::arg("x_min")
    , py::arg("x_max")
    , py::arg("y_min")
    , py::arg("y_max")
    , py::arg("cond") = ImPlotCond_Once
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_legend", &ImPlot::SetupLegend
    , py::arg("location")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_mouse_text", &ImPlot::SetupMouseText
    , py::arg("location")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("setup_finish", &ImPlot::SetupFinish
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_axis_limits", &ImPlot::SetNextAxisLimits
    , py::arg("axis")
    , py::arg("v_min")
    , py::arg("v_max")
    , py::arg("cond") = ImPlotCond_Once
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_axis_links", [](ImAxis axis, double * link_min, double * link_max)
    {
        ImPlot::SetNextAxisLinks(axis, link_min, link_max);
        return std::make_tuple(link_min, link_max);
    }
    , py::arg("axis")
    , py::arg("link_min")
    , py::arg("link_max")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_axis_to_fit", &ImPlot::SetNextAxisToFit
    , py::arg("axis")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_axes_limits", &ImPlot::SetNextAxesLimits
    , py::arg("x_min")
    , py::arg("x_max")
    , py::arg("y_min")
    , py::arg("y_max")
    , py::arg("cond") = ImPlotCond_Once
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_axes_to_fit", &ImPlot::SetNextAxesToFit
    , py::return_value_policy::automatic_reference);
    _aimplot.def("plot_image", &ImPlot::PlotImage
    , py::arg("label_id")
    , py::arg("user_texture_id")
    , py::arg("bounds_min")
    , py::arg("bounds_max")
    , py::arg("uv0") = ImVec2(0,0)
    , py::arg("uv1") = ImVec2(1,1)
    , py::arg("tint_col") = ImVec4(1,1,1,1)
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("plot_text", &ImPlot::PlotText
    , py::arg("text")
    , py::arg("x")
    , py::arg("y")
    , py::arg("pix_offset") = ImVec2(0,0)
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("plot_dummy", &ImPlot::PlotDummy
    , py::arg("label_id")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("drag_point", [](int id, double * x, double * y, const ImVec4 & col, float size, ImPlotDragToolFlags flags)
    {
        auto ret = ImPlot::DragPoint(id, x, y, col, size, flags);
        return std::make_tuple(ret, x, y);
    }
    , py::arg("id")
    , py::arg("x")
    , py::arg("y")
    , py::arg("col")
    , py::arg("size") = 4
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("drag_line_x", [](int id, double * x, const ImVec4 & col, float thickness, ImPlotDragToolFlags flags)
    {
        auto ret = ImPlot::DragLineX(id, x, col, thickness, flags);
        return std::make_tuple(ret, x);
    }
    , py::arg("id")
    , py::arg("x")
    , py::arg("col")
    , py::arg("thickness") = 1
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("drag_line_y", [](int id, double * y, const ImVec4 & col, float thickness, ImPlotDragToolFlags flags)
    {
        auto ret = ImPlot::DragLineY(id, y, col, thickness, flags);
        return std::make_tuple(ret, y);
    }
    , py::arg("id")
    , py::arg("y")
    , py::arg("col")
    , py::arg("thickness") = 1
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("drag_rect", [](int id, double * x1, double * y1, double * x2, double * y2, const ImVec4 & col, ImPlotDragToolFlags flags)
    {
        auto ret = ImPlot::DragRect(id, x1, y1, x2, y2, col, flags);
        return std::make_tuple(ret, x1, y1, x2, y2);
    }
    , py::arg("id")
    , py::arg("x1")
    , py::arg("y1")
    , py::arg("x2")
    , py::arg("y2")
    , py::arg("col")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("annotation", py::overload_cast<double, double, const ImVec4 &, const ImVec2 &, bool, bool>(&ImPlot::Annotation)
    , py::arg("x")
    , py::arg("y")
    , py::arg("col")
    , py::arg("pix_offset")
    , py::arg("clamp")
    , py::arg("round") = false
    , py::return_value_policy::automatic_reference);
    _aimplot.def("annotation", [](double x, double y, const ImVec4 & col, const ImVec2 & pix_offset, bool clamp, const char * fmt)
    {
        ImPlot::Annotation(x, y, col, pix_offset, clamp, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("y")
    , py::arg("col")
    , py::arg("pix_offset")
    , py::arg("clamp")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("tag_x", py::overload_cast<double, const ImVec4 &, bool>(&ImPlot::TagX)
    , py::arg("x")
    , py::arg("col")
    , py::arg("round") = false
    , py::return_value_policy::automatic_reference);
    _aimplot.def("tag_x", [](double x, const ImVec4 & col, const char * fmt)
    {
        ImPlot::TagX(x, col, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("col")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("tag_y", py::overload_cast<double, const ImVec4 &, bool>(&ImPlot::TagY)
    , py::arg("y")
    , py::arg("col")
    , py::arg("round") = false
    , py::return_value_policy::automatic_reference);
    _aimplot.def("tag_y", [](double y, const ImVec4 & col, const char * fmt)
    {
        ImPlot::TagY(y, col, fmt);
        return ;
    }
    , py::arg("y")
    , py::arg("col")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_axis", &ImPlot::SetAxis
    , py::arg("axis")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_axes", &ImPlot::SetAxes
    , py::arg("x_axis")
    , py::arg("y_axis")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("plot_to_pixels", py::overload_cast<const ImPlotPoint &, ImAxis, ImAxis>(&ImPlot::PlotToPixels)
    , py::arg("plt")
    , py::arg("x_axis") = IMPLOT_AUTO
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("plot_to_pixels", py::overload_cast<double, double, ImAxis, ImAxis>(&ImPlot::PlotToPixels)
    , py::arg("x")
    , py::arg("y")
    , py::arg("x_axis") = IMPLOT_AUTO
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_pos", &ImPlot::GetPlotPos
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_size", &ImPlot::GetPlotSize
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_mouse_pos", &ImPlot::GetPlotMousePos
    , py::arg("x_axis") = IMPLOT_AUTO
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_limits", &ImPlot::GetPlotLimits
    , py::arg("x_axis") = IMPLOT_AUTO
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("is_plot_hovered", &ImPlot::IsPlotHovered
    , py::return_value_policy::automatic_reference);
    _aimplot.def("is_axis_hovered", &ImPlot::IsAxisHovered
    , py::arg("axis")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("is_subplots_hovered", &ImPlot::IsSubplotsHovered
    , py::return_value_policy::automatic_reference);
    _aimplot.def("is_plot_selected", &ImPlot::IsPlotSelected
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_selection", &ImPlot::GetPlotSelection
    , py::arg("x_axis") = IMPLOT_AUTO
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("cancel_plot_selection", &ImPlot::CancelPlotSelection
    , py::return_value_policy::automatic_reference);
    _aimplot.def("hide_next_item", &ImPlot::HideNextItem
    , py::arg("hidden") = true
    , py::arg("cond") = ImPlotCond_Once
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_aligned_plots", &ImPlot::BeginAlignedPlots
    , py::arg("group_id")
    , py::arg("vertical") = true
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_aligned_plots", &ImPlot::EndAlignedPlots
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_legend_popup", &ImPlot::BeginLegendPopup
    , py::arg("label_id")
    , py::arg("mouse_button") = 1
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_legend_popup", &ImPlot::EndLegendPopup
    , py::return_value_policy::automatic_reference);
    _aimplot.def("is_legend_entry_hovered", &ImPlot::IsLegendEntryHovered
    , py::arg("label_id")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_target_plot", &ImPlot::BeginDragDropTargetPlot
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_target_axis", &ImPlot::BeginDragDropTargetAxis
    , py::arg("axis")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_target_legend", &ImPlot::BeginDragDropTargetLegend
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_drag_drop_target", &ImPlot::EndDragDropTarget
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_source_plot", &ImPlot::BeginDragDropSourcePlot
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_source_axis", &ImPlot::BeginDragDropSourceAxis
    , py::arg("axis")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("begin_drag_drop_source_item", &ImPlot::BeginDragDropSourceItem
    , py::arg("label_id")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("end_drag_drop_source", &ImPlot::EndDragDropSource
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_style", &ImPlot::GetStyle
    , py::return_value_policy::reference);
    _aimplot.def("style_colors_auto", &ImPlot::StyleColorsAuto
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("style_colors_classic", &ImPlot::StyleColorsClassic
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("style_colors_dark", &ImPlot::StyleColorsDark
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("style_colors_light", &ImPlot::StyleColorsLight
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_style_color", py::overload_cast<ImPlotCol, ImU32>(&ImPlot::PushStyleColor)
    , py::arg("idx")
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_style_color", py::overload_cast<ImPlotCol, const ImVec4 &>(&ImPlot::PushStyleColor)
    , py::arg("idx")
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("pop_style_color", &ImPlot::PopStyleColor
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, float>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, int>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, const ImVec2 &>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("pop_style_var", &ImPlot::PopStyleVar
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_line_style", &ImPlot::SetNextLineStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("weight") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_fill_style", &ImPlot::SetNextFillStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("alpha_mod") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_marker_style", &ImPlot::SetNextMarkerStyle
    , py::arg("marker") = IMPLOT_AUTO
    , py::arg("size") = IMPLOT_AUTO
    , py::arg("fill") = IMPLOT_AUTO_COL
    , py::arg("weight") = IMPLOT_AUTO
    , py::arg("outline") = IMPLOT_AUTO_COL
    , py::return_value_policy::automatic_reference);
    _aimplot.def("set_next_error_bar_style", &ImPlot::SetNextErrorBarStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("size") = IMPLOT_AUTO
    , py::arg("weight") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_last_item_color", &ImPlot::GetLastItemColor
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_style_color_name", &ImPlot::GetStyleColorName
    , py::arg("idx")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_marker_name", &ImPlot::GetMarkerName
    , py::arg("idx")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("add_colormap", py::overload_cast<const char *, const ImVec4 *, int, bool>(&ImPlot::AddColormap)
    , py::arg("name")
    , py::arg("cols")
    , py::arg("size")
    , py::arg("qual") = true
    , py::return_value_policy::automatic_reference);
    _aimplot.def("add_colormap", py::overload_cast<const char *, const ImU32 *, int, bool>(&ImPlot::AddColormap)
    , py::arg("name")
    , py::arg("cols")
    , py::arg("size")
    , py::arg("qual") = true
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_colormap_count", &ImPlot::GetColormapCount
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_colormap_name", &ImPlot::GetColormapName
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_colormap_index", &ImPlot::GetColormapIndex
    , py::arg("name")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_colormap", py::overload_cast<ImPlotColormap>(&ImPlot::PushColormap)
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_colormap", py::overload_cast<const char *>(&ImPlot::PushColormap)
    , py::arg("name")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("pop_colormap", &ImPlot::PopColormap
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    _aimplot.def("next_colormap_color", &ImPlot::NextColormapColor
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_colormap_size", &ImPlot::GetColormapSize
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_colormap_color", &ImPlot::GetColormapColor
    , py::arg("idx")
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("sample_colormap", &ImPlot::SampleColormap
    , py::arg("t")
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("colormap_scale", &ImPlot::ColormapScale
    , py::arg("label")
    , py::arg("scale_min")
    , py::arg("scale_max")
    , py::arg("size") = ImVec2(0,0)
    , py::arg("format") = nullptr
    , py::arg("flags") = 0
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("colormap_slider", [](const char * label, float * t, ImVec4 * out, const char * format, ImPlotColormap cmap)
    {
        auto ret = ImPlot::ColormapSlider(label, t, out, format, cmap);
        return std::make_tuple(ret, t);
    }
    , py::arg("label")
    , py::arg("t")
    , py::arg("out") = nullptr
    , py::arg("format") = nullptr
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("colormap_button", &ImPlot::ColormapButton
    , py::arg("label")
    , py::arg("size") = ImVec2(0,0)
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    _aimplot.def("bust_color_cache", &ImPlot::BustColorCache
    , py::arg("plot_title_id") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_input_map", &ImPlot::GetInputMap
    , py::return_value_policy::reference);
    _aimplot.def("map_input_default", &ImPlot::MapInputDefault
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("map_input_reverse", &ImPlot::MapInputReverse
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("item_icon", py::overload_cast<const ImVec4 &>(&ImPlot::ItemIcon)
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("item_icon", py::overload_cast<ImU32>(&ImPlot::ItemIcon)
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("colormap_icon", &ImPlot::ColormapIcon
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("get_plot_draw_list", &ImPlot::GetPlotDrawList
    , py::return_value_policy::automatic_reference);
    _aimplot.def("push_plot_clip_rect", &ImPlot::PushPlotClipRect
    , py::arg("expand") = 0
    , py::return_value_policy::automatic_reference);
    _aimplot.def("pop_plot_clip_rect", &ImPlot::PopPlotClipRect
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_style_selector", &ImPlot::ShowStyleSelector
    , py::arg("label")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_colormap_selector", &ImPlot::ShowColormapSelector
    , py::arg("label")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_input_map_selector", &ImPlot::ShowInputMapSelector
    , py::arg("label")
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_style_editor", &ImPlot::ShowStyleEditor
    , py::arg("ref") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_user_guide", &ImPlot::ShowUserGuide
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_metrics_window", [](bool * p_popen)
    {
        ImPlot::ShowMetricsWindow(p_popen);
        return p_popen;
    }
    , py::arg("p_popen") = nullptr
    , py::return_value_policy::automatic_reference);
    _aimplot.def("show_demo_window", [](bool * p_open)
    {
        ImPlot::ShowDemoWindow(p_open);
        return p_open;
    }
    , py::arg("p_open") = nullptr
    , py::return_value_policy::automatic_reference);

}