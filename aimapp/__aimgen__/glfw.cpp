#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <GLFW/glfw3.h>
struct GLFWmonitor {};
struct GLFWwindow {};
struct GLFWcursor {};

#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_glfw(py::module &libaimapp, Registry &registry) {
{{body}}
}