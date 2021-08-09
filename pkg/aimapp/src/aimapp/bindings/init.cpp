#include <pybind11/pybind11.h>

#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_main(py::module &, Registry& registry);
//void init_glfw(py::module &, Registry& registry);


PYBIND11_MODULE(libaimapp, m) {
        Registry r;
        init_main(m, r);
        //init_glfw(m, r);
}