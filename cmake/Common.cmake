set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 17)
# Set default compile flags for GCC
if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-format-security")
endif(CMAKE_COMPILER_IS_GNUCXX)

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

cmake_path(SET BUILD_DIR "$ENV{VIRTUAL_ENV}/Build/cmake")
#list(APPEND CMAKE_MODULE_PATH ${BUILD_DIR})
list(APPEND CMAKE_PREFIX_PATH ${BUILD_DIR})

set(MONO_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

set(IMGUI_DIR ${MONO_DIR}/imgui)

add_subdirectory(${MONO_DIR}/pybind11 build)

set(IMGUI_HEADERS
    ${IMGUI_DIR}/imconfig.h
    ${IMGUI_DIR}/imgui_internal.h
    ${IMGUI_DIR}/imgui.h
    ${IMGUI_DIR}/imstb_rectpack.h
    ${IMGUI_DIR}/imstb_textedit.h
    ${IMGUI_DIR}/imstb_truetype.h
)

set(AIMGUI_DIR ${MONO_DIR}/aimgui)
set(IMGUI_DIR ${MONO_DIR}/imgui)

#list(APPEND CMAKE_MODULE_PATH "${AIMGUI_DIR}/cmake")

include(${CMAKE_CURRENT_LIST_DIR}/Functions.cmake)