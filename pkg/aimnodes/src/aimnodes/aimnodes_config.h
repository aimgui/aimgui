#pragma once

#include <pybind11/functional.h>

namespace pybind11 {

inline bool PyWrapper_Check(PyObject *o) { return true; }

class wrapper : public object {
public:
    PYBIND11_OBJECT_DEFAULT(wrapper, object, PyWrapper_Check)
    wrapper(void* x) { m_ptr = (PyObject*)x; }
    explicit operator bool() const { return m_ptr != nullptr && m_ptr != Py_None; }
};

} //namespace pybind11

namespace py = pybind11;

#define ImNodesMiniMapNodeHoveringCallback py::wrapper

#define ImNodesMiniMapNodeHoveringCallbackUserData py::wrapper
