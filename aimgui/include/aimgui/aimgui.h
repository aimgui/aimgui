#include <pybind11/pybind11.h>

namespace py = pybind11;

typedef ImVector<ImDrawCmd> AimCmdBuffer;
typedef ImVector<ImDrawIdx> AimIdxBuffer;
typedef ImVector<ImDrawVert> AimVtxBuffer;

struct AimDrawList {
    static const size_t COMMAND_SIZE = sizeof(ImDrawCmd);
    static const size_t VERTEX_SIZE = sizeof(ImDrawVert);
    static const size_t INDEX_SIZE = sizeof(ImDrawIdx);
    static const size_t CMD_BUFFER_SIZE = sizeof(AimCmdBuffer);
    static const size_t IDX_BUFFER_SIZE = sizeof(AimIdxBuffer);
    static const size_t VTX_BUFFER_SIZE = sizeof(AimVtxBuffer);
};

struct AimIO {
};

template<typename T>
void template_ImVector(py::module &module, const char* name)
{
    py::class_< ImVector<T> >(module, name)
        .def_property_readonly_static("stride", [](py::object)
        {
            return sizeof(T);
        })
        .def_property_readonly("data", [](const ImVector<T>& self)
        {
            return long((void*)self.Data);
        })
        .def("__len__", [](const ImVector<T>& self)
        {
            return self.size();
        })
        .def("__iter__", [](const ImVector<T>& self)
        {
            return py::make_iterator(self.begin(), self.end());
        })
        .def("__getitem__", [](const ImVector<T>& self, size_t i)
        {
            if ((int)i >= self.size()) throw py::index_error();
            return self[i];
        })
        ;
}
