#include <limits>
#include <filesystem>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

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

}

