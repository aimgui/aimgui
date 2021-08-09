#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "implot.h"
#include "implot_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_main(py::module &libaimplot, Registry &registry) {
    /*
        ImPlotContext needs to be an opaque type.  Wrap it with PyCapsule
    */
    //IMPLOT_API ImPlotContext* CreateContext();
    libaimplot.def("create_context", []()
    {
        return py::capsule(ImPlot::CreateContext(), "ImPlotContext");
    }
    , py::return_value_policy::automatic_reference);

    //IMPLOT_API void DestroyContext(ImPlotContext* ctx = NULL);
    libaimplot.def("destroy_context", [](py::capsule& ctx)
    {
        ImPlot::DestroyContext(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //IMPLOT_API ImPlotContext* GetCurrentContext();
    libaimplot.def("get_current_context", []()
    {
        return (void*)ImPlot::GetCurrentContext();
    }
    , py::return_value_policy::automatic_reference);

    //IMPLOT_API void SetCurrentContext(ImPlotContext* ctx);
    libaimplot.def("set_current_context", [](py::capsule& ctx)
    {
        ImPlot::SetCurrentContext(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API void PlotLine(const char* label_id, const T* values, int count, double xscale=1, double x0=0, int offset=0, int stride=sizeof(T));
    libaimplot.def("plot_line", [](const char* label_id, const py::array_t<double>& values, int count)
    {
        ImPlot::PlotLine<double>(label_id, (double*)values.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template IMPLOT_API void PlotLine<double>(const char* label_id, const double* xs, const double* ys, int count, int offset, int stride);
    libaimplot.def("plot_line", [](const char* label_id, const py::array_t<double>& xs, const py::array_t<double>& ys, int count)
    {
        ImPlot::PlotLine<double>(label_id, (double*)xs.unchecked().data(), (double*)ys.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("xs")
    , py::arg("ys")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API  void PlotScatter(const char* label_id, const T* values, int count, double xscale=1, double x0=0, int offset=0, int stride=sizeof(T));
    libaimplot.def("plot_scatter", [](const char* label_id, const py::array_t<double>& values, int count)
    {
        ImPlot::PlotScatter<double>(label_id, (double*)values.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API void PlotShaded(const char* label_id, const T* values, int count, double y_ref=0, double xscale=1, double x0=0, int offset=0, int stride=sizeof(T));
    libaimplot.def("plot_shaded", [](const char* label_id, const py::array_t<double>& values, int count)
    {
        ImPlot::PlotShaded<double>(label_id, (double*)values.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API void PlotBars(const char* label_id, const T* values, int count, double width=0.67, double shift=0, int offset=0, int stride=sizeof(T));
    libaimplot.def("plot_bars", [](const char* label_id, const py::array_t<double>& values, int count)
    {
        ImPlot::PlotBars<double>(label_id, (double*)values.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API void PlotBarsH(const char* label_id, const T* values, int count, double height=0.67, double shift=0, int offset=0, int stride=sizeof(T));
    libaimplot.def("plot_bars_h", [](const char* label_id, const py::array_t<double>& values, int count)
    {
        ImPlot::PlotBarsH<double>(label_id, (double*)values.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);

    //template <typename T> IMPLOT_API void PlotErrorBars(const char* label_id, const T* xs, const T* ys, const T* err, int count, int offset=0, int stride=sizeof(T));
    /* TODO: Put this one off until I understand it!
    libaimplot.def("plot_error_bars", [](const char* label_id, const py::array_t<double>& xs, const py::array_t<double>& ys, const py::array_t<double>& err int count)
    {
        ImPlot::PlotErrorBars<double>(label_id, (double*)xs.unchecked().data(), (double*)ys.unchecked().data(), (double*)err.unchecked().data(), count);
    }
    , py::arg("label_id")
    , py::arg("values")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    */
}

