#include <pybind11/pybind11.h>

namespace py = pybind11;

using namespace ax::NodeEditor;

namespace pybind11 { namespace detail {

    template <> struct type_caster<NodeId> {
    public:
        PYBIND11_TYPE_CASTER(NodeId, _("NodeId"));
        bool load(handle src, bool implicit) {
            PyObject *source = src.ptr();
            value = PyLong_AsLong(source);
            return !PyErr_Occurred();
        }
        static handle cast(NodeId src, return_value_policy /* policy */, handle /* parent */) {
            auto result = PyLong_FromLong(src.Get());
            return result;
        }
    };

    template <> struct type_caster<PinId> {
    public:
        PYBIND11_TYPE_CASTER(PinId, _("PinId"));
        bool load(handle src, bool implicit) {
            PyObject *source = src.ptr();
            value = PyLong_AsLong(source);
            return !PyErr_Occurred();
        }
        static handle cast(PinId src, return_value_policy /* policy */, handle /* parent */) {
            auto result = PyLong_FromLong(src.Get());
            return result;
        }
    };

    template <> struct type_caster<LinkId> {
    public:
        PYBIND11_TYPE_CASTER(LinkId, _("LinkId"));
        bool load(handle src, bool implicit) {
            PyObject *source = src.ptr();
            value = PyLong_AsLong(source);
            return !PyErr_Occurred();
        }
        static handle cast(LinkId src, return_value_policy /* policy */, handle /* parent */) {
            auto result = PyLong_FromLong(src.Get());
            return result;
        }
    };

}} // namespace pybind11::detail