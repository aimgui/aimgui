#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace pybind11 { namespace detail {

    template <> struct type_caster<ImVec2> {
    public:
        PYBIND11_TYPE_CASTER(ImVec2, _("Vec2"));
        bool load(handle src, bool implicit) {
            PyObject *source = src.ptr();
            value[0] = PyFloat_AsDouble(PyTuple_GetItem(source, 0));
            value[1] = PyFloat_AsDouble(PyTuple_GetItem(source, 1));
            return !PyErr_Occurred();
        }
        static handle cast(ImVec2 src, return_value_policy /* policy */, handle /* parent */) {
            auto tuple = PyTuple_New(2);
            PyTuple_SetItem(tuple, 0, PyFloat_FromDouble(src[0]));
            PyTuple_SetItem(tuple, 1, PyFloat_FromDouble(src[1]));
            return tuple;
        }
    };

    template <> struct type_caster<ImVec4> {
    public:
        PYBIND11_TYPE_CASTER(ImVec4, _("Vec4"));
        bool load(handle src, bool implicit) {
            PyObject *source = src.ptr();
            value.x = PyFloat_AsDouble(PyTuple_GetItem(source, 0));
            value.y = PyFloat_AsDouble(PyTuple_GetItem(source, 1));
            value.z = PyFloat_AsDouble(PyTuple_GetItem(source, 2));
            value.w = PyFloat_AsDouble(PyTuple_GetItem(source, 3));
            return !PyErr_Occurred();
        }
        static handle cast(ImVec4 src, return_value_policy /* policy */, handle /* parent */) {
            // auto result = py::make_tuple(src.x, src.y, src.z, src.w);
            auto result = PyTuple_New(4);
            PyTuple_SetItem(result, 0, PyFloat_FromDouble(src.x));
            PyTuple_SetItem(result, 1, PyFloat_FromDouble(src.y));
            PyTuple_SetItem(result, 2, PyFloat_FromDouble(src.z));
            PyTuple_SetItem(result, 3, PyFloat_FromDouble(src.w));
            return result;
        }
    };

}} // namespace pybind11::detail