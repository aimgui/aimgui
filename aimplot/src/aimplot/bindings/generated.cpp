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

void init_generated(py::module &libaimplot, Registry &registry) {

    py::enum_<ImPlotFlags_>(libaimplot, "Flags", py::arithmetic())
        .value("FLAGS_NONE", ImPlotFlags_None)
        .value("FLAGS_NO_TITLE", ImPlotFlags_NoTitle)
        .value("FLAGS_NO_LEGEND", ImPlotFlags_NoLegend)
        .value("FLAGS_NO_MENUS", ImPlotFlags_NoMenus)
        .value("FLAGS_NO_BOX_SELECT", ImPlotFlags_NoBoxSelect)
        .value("FLAGS_NO_MOUSE_POS", ImPlotFlags_NoMousePos)
        .value("FLAGS_NO_HIGHLIGHT", ImPlotFlags_NoHighlight)
        .value("FLAGS_NO_CHILD", ImPlotFlags_NoChild)
        .value("FLAGS_EQUAL", ImPlotFlags_Equal)
        .value("FLAGS_Y_AXIS2", ImPlotFlags_YAxis2)
        .value("FLAGS_Y_AXIS3", ImPlotFlags_YAxis3)
        .value("FLAGS_QUERY", ImPlotFlags_Query)
        .value("FLAGS_CROSSHAIRS", ImPlotFlags_Crosshairs)
        .value("FLAGS_ANTI_ALIASED", ImPlotFlags_AntiAliased)
        .value("FLAGS_CANVAS_ONLY", ImPlotFlags_CanvasOnly)
        .export_values();

    py::enum_<ImPlotAxisFlags_>(libaimplot, "AxisFlags", py::arithmetic())
        .value("AXIS_FLAGS_NONE", ImPlotAxisFlags_None)
        .value("AXIS_FLAGS_NO_LABEL", ImPlotAxisFlags_NoLabel)
        .value("AXIS_FLAGS_NO_GRID_LINES", ImPlotAxisFlags_NoGridLines)
        .value("AXIS_FLAGS_NO_TICK_MARKS", ImPlotAxisFlags_NoTickMarks)
        .value("AXIS_FLAGS_NO_TICK_LABELS", ImPlotAxisFlags_NoTickLabels)
        .value("AXIS_FLAGS_FOREGROUND", ImPlotAxisFlags_Foreground)
        .value("AXIS_FLAGS_LOG_SCALE", ImPlotAxisFlags_LogScale)
        .value("AXIS_FLAGS_TIME", ImPlotAxisFlags_Time)
        .value("AXIS_FLAGS_INVERT", ImPlotAxisFlags_Invert)
        .value("AXIS_FLAGS_NO_INITIAL_FIT", ImPlotAxisFlags_NoInitialFit)
        .value("AXIS_FLAGS_AUTO_FIT", ImPlotAxisFlags_AutoFit)
        .value("AXIS_FLAGS_RANGE_FIT", ImPlotAxisFlags_RangeFit)
        .value("AXIS_FLAGS_LOCK_MIN", ImPlotAxisFlags_LockMin)
        .value("AXIS_FLAGS_LOCK_MAX", ImPlotAxisFlags_LockMax)
        .value("AXIS_FLAGS_LOCK", ImPlotAxisFlags_Lock)
        .value("AXIS_FLAGS_NO_DECORATIONS", ImPlotAxisFlags_NoDecorations)
        .export_values();

    py::enum_<ImPlotCol_>(libaimplot, "Col", py::arithmetic())
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
        .value("COL_X_AXIS", ImPlotCol_XAxis)
        .value("COL_X_AXIS_GRID", ImPlotCol_XAxisGrid)
        .value("COL_Y_AXIS", ImPlotCol_YAxis)
        .value("COL_Y_AXIS_GRID", ImPlotCol_YAxisGrid)
        .value("COL_Y_AXIS2", ImPlotCol_YAxis2)
        .value("COL_Y_AXIS_GRID2", ImPlotCol_YAxisGrid2)
        .value("COL_Y_AXIS3", ImPlotCol_YAxis3)
        .value("COL_Y_AXIS_GRID3", ImPlotCol_YAxisGrid3)
        .value("COL_SELECTION", ImPlotCol_Selection)
        .value("COL_QUERY", ImPlotCol_Query)
        .value("COL_CROSSHAIRS", ImPlotCol_Crosshairs)
        .value("COL_COUNT", ImPlotCol_COUNT)
        .export_values();

    py::enum_<ImPlotStyleVar_>(libaimplot, "StyleVar", py::arithmetic())
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

    py::enum_<ImPlotMarker_>(libaimplot, "Marker", py::arithmetic())
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

    py::enum_<ImPlotColormap_>(libaimplot, "Colormap", py::arithmetic())
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

    py::enum_<ImPlotLocation_>(libaimplot, "Location", py::arithmetic())
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

    py::enum_<ImPlotOrientation_>(libaimplot, "Orientation", py::arithmetic())
        .value("ORIENTATION_HORIZONTAL", ImPlotOrientation_Horizontal)
        .value("ORIENTATION_VERTICAL", ImPlotOrientation_Vertical)
        .export_values();

    py::enum_<ImPlotYAxis_>(libaimplot, "YAxis", py::arithmetic())
        .value("Y_AXIS_1", ImPlotYAxis_1)
        .value("Y_AXIS_2", ImPlotYAxis_2)
        .value("Y_AXIS_3", ImPlotYAxis_3)
        .export_values();

    py::enum_<ImPlotBin_>(libaimplot, "Bin", py::arithmetic())
        .value("BIN_SQRT", ImPlotBin_Sqrt)
        .value("BIN_STURGES", ImPlotBin_Sturges)
        .value("BIN_RICE", ImPlotBin_Rice)
        .value("BIN_SCOTT", ImPlotBin_Scott)
        .export_values();

        PYCLASS_BEGIN(libaimplot, ImPlotPoint, Point)
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
    PYCLASS_END(libaimplot, ImPlotPoint, Point)


        PYCLASS_BEGIN(libaimplot, ImPlotRange, Range)
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
    PYCLASS_END(libaimplot, ImPlotRange, Range)


        PYCLASS_BEGIN(libaimplot, ImPlotLimits, Limits)
    Limits.def_readwrite("x", &ImPlotLimits::X);
    Limits.def_readwrite("y", &ImPlotLimits::Y);
    Limits.def(py::init<>());
    Limits.def(py::init<double, double, double, double>()
    , py::arg("x_min")
    , py::arg("x_max")
    , py::arg("y_min")
    , py::arg("y_max")
    );
    Limits.def("min", &ImPlotLimits::Min
    , py::return_value_policy::automatic_reference);
    Limits.def("max", &ImPlotLimits::Max
    , py::return_value_policy::automatic_reference);
    PYCLASS_END(libaimplot, ImPlotLimits, Limits)


        PYCLASS_BEGIN(libaimplot, ImPlotStyle, Style)
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
    Style.def_readwrite("anti_aliased_lines", &ImPlotStyle::AntiAliasedLines);
    Style.def_readwrite("use_local_time", &ImPlotStyle::UseLocalTime);
    Style.def_readwrite("use_iso8601", &ImPlotStyle::UseISO8601);
    Style.def_readwrite("use24_hour_clock", &ImPlotStyle::Use24HourClock);
    Style.def(py::init<>());
    PYCLASS_END(libaimplot, ImPlotStyle, Style)


    libaimplot.def("set_im_gui_context", &ImPlot::SetImGuiContext
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_plot", &ImPlot::BeginPlot
    , py::arg("title_id")
    , py::arg("x_label") = nullptr
    , py::arg("y_label") = nullptr
    , py::arg("size") = ImVec2(-1,0)
    , py::arg("flags") = ImPlotFlags_None
    , py::arg("x_flags") = ImPlotAxisFlags_None
    , py::arg("y_flags") = ImPlotAxisFlags_None
    , py::arg("y2_flags") = ImPlotAxisFlags_NoGridLines
    , py::arg("y3_flags") = ImPlotAxisFlags_NoGridLines
    , py::arg("y2_label") = nullptr
    , py::arg("y3_label") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("end_plot", &ImPlot::EndPlot
    , py::return_value_policy::automatic_reference);
    libaimplot.def("plot_image", &ImPlot::PlotImage
    , py::arg("label_id")
    , py::arg("user_texture_id")
    , py::arg("bounds_min")
    , py::arg("bounds_max")
    , py::arg("uv0") = ImVec2(0,0)
    , py::arg("uv1") = ImVec2(1,1)
    , py::arg("tint_col") = ImVec4(1,1,1,1)
    , py::return_value_policy::automatic_reference);
    libaimplot.def("plot_text", &ImPlot::PlotText
    , py::arg("text")
    , py::arg("x")
    , py::arg("y")
    , py::arg("vertical") = false
    , py::arg("pix_offset") = ImVec2(0,0)
    , py::return_value_policy::automatic_reference);
    libaimplot.def("plot_dummy", &ImPlot::PlotDummy
    , py::arg("label_id")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_plot_limits", &ImPlot::SetNextPlotLimits
    , py::arg("xmin")
    , py::arg("xmax")
    , py::arg("ymin")
    , py::arg("ymax")
    , py::arg("cond") = ImGuiCond_Once
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_plot_limits_x", &ImPlot::SetNextPlotLimitsX
    , py::arg("xmin")
    , py::arg("xmax")
    , py::arg("cond") = ImGuiCond_Once
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_plot_limits_y", &ImPlot::SetNextPlotLimitsY
    , py::arg("ymin")
    , py::arg("ymax")
    , py::arg("cond") = ImGuiCond_Once
    , py::arg("y_axis") = ImPlotYAxis_1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("link_next_plot_limits", [](double * xmin, double * xmax, double * ymin, double * ymax, double * ymin2, double * ymax2, double * ymin3, double * ymax3)
    {
        ImPlot::LinkNextPlotLimits(xmin, xmax, ymin, ymax, ymin2, ymax2, ymin3, ymax3);
        return std::make_tuple(xmin, xmax, ymin, ymax, ymin2, ymax2, ymin3, ymax3);
    }
    , py::arg("xmin")
    , py::arg("xmax")
    , py::arg("ymin")
    , py::arg("ymax")
    , py::arg("ymin2") = nullptr
    , py::arg("ymax2") = nullptr
    , py::arg("ymin3") = nullptr
    , py::arg("ymax3") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("fit_next_plot_axes", &ImPlot::FitNextPlotAxes
    , py::arg("x") = true
    , py::arg("y") = true
    , py::arg("y2") = true
    , py::arg("y3") = true
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_plot_format_x", &ImPlot::SetNextPlotFormatX
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_plot_format_y", &ImPlot::SetNextPlotFormatY
    , py::arg("fmt")
    , py::arg("y_axis") = ImPlotYAxis_1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_plot_y_axis", &ImPlot::SetPlotYAxis
    , py::arg("y_axis")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("hide_next_item", &ImPlot::HideNextItem
    , py::arg("hidden") = true
    , py::arg("cond") = ImGuiCond_Once
    , py::return_value_policy::automatic_reference);
    libaimplot.def("plot_to_pixels", py::overload_cast<const ImPlotPoint &, ImPlotYAxis>(&ImPlot::PlotToPixels)
    , py::arg("plt")
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("plot_to_pixels", py::overload_cast<double, double, ImPlotYAxis>(&ImPlot::PlotToPixels)
    , py::arg("x")
    , py::arg("y")
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_pos", &ImPlot::GetPlotPos
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_size", &ImPlot::GetPlotSize
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_plot_hovered", &ImPlot::IsPlotHovered
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_plot_x_axis_hovered", &ImPlot::IsPlotXAxisHovered
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_plot_y_axis_hovered", &ImPlot::IsPlotYAxisHovered
    , py::arg("y_axis") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_mouse_pos", &ImPlot::GetPlotMousePos
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_limits", &ImPlot::GetPlotLimits
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_plot_selected", &ImPlot::IsPlotSelected
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_selection", &ImPlot::GetPlotSelection
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_plot_queried", &ImPlot::IsPlotQueried
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_query", &ImPlot::GetPlotQuery
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_plot_query", &ImPlot::SetPlotQuery
    , py::arg("query")
    , py::arg("y_axis") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("annotate", [](double x, double y, const ImVec2 & pix_offset, const char * fmt)
    {
        ImPlot::Annotate(x, y, pix_offset, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("y")
    , py::arg("pix_offset")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("annotate", [](double x, double y, const ImVec2 & pix_offset, const ImVec4 & color, const char * fmt)
    {
        ImPlot::Annotate(x, y, pix_offset, color, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("y")
    , py::arg("pix_offset")
    , py::arg("color")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("annotate_clamped", [](double x, double y, const ImVec2 & pix_offset, const char * fmt)
    {
        ImPlot::AnnotateClamped(x, y, pix_offset, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("y")
    , py::arg("pix_offset")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("annotate_clamped", [](double x, double y, const ImVec2 & pix_offset, const ImVec4 & color, const char * fmt)
    {
        ImPlot::AnnotateClamped(x, y, pix_offset, color, fmt);
        return ;
    }
    , py::arg("x")
    , py::arg("y")
    , py::arg("pix_offset")
    , py::arg("color")
    , py::arg("fmt")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("drag_line_x", [](const char * id, double * x_value, bool show_label, const ImVec4 & col, float thickness)
    {
        auto ret = ImPlot::DragLineX(id, x_value, show_label, col, thickness);
        return std::make_tuple(ret, x_value);
    }
    , py::arg("id")
    , py::arg("x_value")
    , py::arg("show_label") = true
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("thickness") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("drag_line_y", [](const char * id, double * y_value, bool show_label, const ImVec4 & col, float thickness)
    {
        auto ret = ImPlot::DragLineY(id, y_value, show_label, col, thickness);
        return std::make_tuple(ret, y_value);
    }
    , py::arg("id")
    , py::arg("y_value")
    , py::arg("show_label") = true
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("thickness") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("drag_point", [](const char * id, double * x, double * y, bool show_label, const ImVec4 & col, float radius)
    {
        auto ret = ImPlot::DragPoint(id, x, y, show_label, col, radius);
        return std::make_tuple(ret, x, y);
    }
    , py::arg("id")
    , py::arg("x")
    , py::arg("y")
    , py::arg("show_label") = true
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("radius") = 4
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_legend_location", &ImPlot::SetLegendLocation
    , py::arg("location")
    , py::arg("orientation") = ImPlotOrientation_Vertical
    , py::arg("outside") = false
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_mouse_pos_location", &ImPlot::SetMousePosLocation
    , py::arg("location")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("is_legend_entry_hovered", &ImPlot::IsLegendEntryHovered
    , py::arg("label_id")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_legend_popup", &ImPlot::BeginLegendPopup
    , py::arg("label_id")
    , py::arg("mouse_button") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("end_legend_popup", &ImPlot::EndLegendPopup
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_target", &ImPlot::BeginDragDropTarget
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_target_x", &ImPlot::BeginDragDropTargetX
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_target_y", &ImPlot::BeginDragDropTargetY
    , py::arg("axis") = ImPlotYAxis_1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_target_legend", &ImPlot::BeginDragDropTargetLegend
    , py::return_value_policy::automatic_reference);
    libaimplot.def("end_drag_drop_target", &ImPlot::EndDragDropTarget
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_source", &ImPlot::BeginDragDropSource
    , py::arg("key_mods") = ImGuiKeyModFlags_Ctrl
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_source_x", &ImPlot::BeginDragDropSourceX
    , py::arg("key_mods") = ImGuiKeyModFlags_Ctrl
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_source_y", &ImPlot::BeginDragDropSourceY
    , py::arg("axis") = ImPlotYAxis_1
    , py::arg("key_mods") = ImGuiKeyModFlags_Ctrl
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("begin_drag_drop_source_item", &ImPlot::BeginDragDropSourceItem
    , py::arg("label_id")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("end_drag_drop_source", &ImPlot::EndDragDropSource
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_style", &ImPlot::GetStyle
    , py::return_value_policy::reference);
    libaimplot.def("style_colors_auto", &ImPlot::StyleColorsAuto
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("style_colors_classic", &ImPlot::StyleColorsClassic
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("style_colors_dark", &ImPlot::StyleColorsDark
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("style_colors_light", &ImPlot::StyleColorsLight
    , py::arg("dst") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_style_color", py::overload_cast<ImPlotCol, ImU32>(&ImPlot::PushStyleColor)
    , py::arg("idx")
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_style_color", py::overload_cast<ImPlotCol, const ImVec4 &>(&ImPlot::PushStyleColor)
    , py::arg("idx")
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("pop_style_color", &ImPlot::PopStyleColor
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, float>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, int>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_style_var", py::overload_cast<ImPlotStyleVar, const ImVec2 &>(&ImPlot::PushStyleVar)
    , py::arg("idx")
    , py::arg("val")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("pop_style_var", &ImPlot::PopStyleVar
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_line_style", &ImPlot::SetNextLineStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("weight") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_fill_style", &ImPlot::SetNextFillStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("alpha_mod") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_marker_style", &ImPlot::SetNextMarkerStyle
    , py::arg("marker") = IMPLOT_AUTO
    , py::arg("size") = IMPLOT_AUTO
    , py::arg("fill") = IMPLOT_AUTO_COL
    , py::arg("weight") = IMPLOT_AUTO
    , py::arg("outline") = IMPLOT_AUTO_COL
    , py::return_value_policy::automatic_reference);
    libaimplot.def("set_next_error_bar_style", &ImPlot::SetNextErrorBarStyle
    , py::arg("col") = IMPLOT_AUTO_COL
    , py::arg("size") = IMPLOT_AUTO
    , py::arg("weight") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_last_item_color", &ImPlot::GetLastItemColor
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_style_color_name", &ImPlot::GetStyleColorName
    , py::arg("idx")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_marker_name", &ImPlot::GetMarkerName
    , py::arg("idx")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("add_colormap", py::overload_cast<const char *, const ImVec4 *, int, bool>(&ImPlot::AddColormap)
    , py::arg("name")
    , py::arg("cols")
    , py::arg("size")
    , py::arg("qual") = true
    , py::return_value_policy::automatic_reference);
    libaimplot.def("add_colormap", py::overload_cast<const char *, const ImU32 *, int, bool>(&ImPlot::AddColormap)
    , py::arg("name")
    , py::arg("cols")
    , py::arg("size")
    , py::arg("qual") = true
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_colormap_count", &ImPlot::GetColormapCount
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_colormap_name", &ImPlot::GetColormapName
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_colormap_index", &ImPlot::GetColormapIndex
    , py::arg("name")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_colormap", py::overload_cast<ImPlotColormap>(&ImPlot::PushColormap)
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_colormap", py::overload_cast<const char *>(&ImPlot::PushColormap)
    , py::arg("name")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("pop_colormap", &ImPlot::PopColormap
    , py::arg("count") = 1
    , py::return_value_policy::automatic_reference);
    libaimplot.def("next_colormap_color", &ImPlot::NextColormapColor
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_colormap_size", &ImPlot::GetColormapSize
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_colormap_color", &ImPlot::GetColormapColor
    , py::arg("idx")
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("sample_colormap", &ImPlot::SampleColormap
    , py::arg("t")
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("colormap_scale", &ImPlot::ColormapScale
    , py::arg("label")
    , py::arg("scale_min")
    , py::arg("scale_max")
    , py::arg("size") = ImVec2(0,0)
    , py::arg("cmap") = IMPLOT_AUTO
    , py::arg("fmt") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("colormap_slider", [](const char * label, float * t, ImVec4 * out, const char * format, ImPlotColormap cmap)
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
    libaimplot.def("colormap_button", &ImPlot::ColormapButton
    , py::arg("label")
    , py::arg("size") = ImVec2(0,0)
    , py::arg("cmap") = IMPLOT_AUTO
    , py::return_value_policy::automatic_reference);
    libaimplot.def("bust_color_cache", &ImPlot::BustColorCache
    , py::arg("plot_title_id") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("item_icon", py::overload_cast<const ImVec4 &>(&ImPlot::ItemIcon)
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("item_icon", py::overload_cast<ImU32>(&ImPlot::ItemIcon)
    , py::arg("col")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("colormap_icon", &ImPlot::ColormapIcon
    , py::arg("cmap")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("get_plot_draw_list", &ImPlot::GetPlotDrawList
    , py::return_value_policy::automatic_reference);
    libaimplot.def("push_plot_clip_rect", &ImPlot::PushPlotClipRect
    , py::arg("expand") = 0
    , py::return_value_policy::automatic_reference);
    libaimplot.def("pop_plot_clip_rect", &ImPlot::PopPlotClipRect
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_style_selector", &ImPlot::ShowStyleSelector
    , py::arg("label")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_colormap_selector", &ImPlot::ShowColormapSelector
    , py::arg("label")
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_style_editor", &ImPlot::ShowStyleEditor
    , py::arg("ref") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_user_guide", &ImPlot::ShowUserGuide
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_metrics_window", [](bool * p_popen)
    {
        ImPlot::ShowMetricsWindow(p_popen);
        return p_popen;
    }
    , py::arg("p_popen") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimplot.def("show_demo_window", [](bool * p_open)
    {
        ImPlot::ShowDemoWindow(p_open);
        return p_open;
    }
    , py::arg("p_open") = nullptr
    , py::return_value_policy::automatic_reference);

}