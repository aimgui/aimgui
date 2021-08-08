#include <pybind11/pybind11.h>

#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_main(py::module &, Registry& registry);
void init_bgfx(py::module &, Registry& registry);
void init_platform(py::module&, Registry& registry);
void init_embedded_shader(py::module&, Registry& registry);


PYBIND11_MODULE(libaimgfx, m) {
        Registry r;
        init_main(m, r);
        init_bgfx(m, r);
        init_platform(m, r);
}