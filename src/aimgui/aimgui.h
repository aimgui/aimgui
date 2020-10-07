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