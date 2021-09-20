include_guard()

include(${CMAKE_CURRENT_LIST_DIR}/Standard.cmake)

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

#TODO:Need CMake 3.20 to use cmake_path
#cmake_path(SET BUILD_DIR "$ENV{VIRTUAL_ENV}/Build/cmake")
set(BUILD_DIR "$ENV{VIRTUAL_ENV}/Build/cmake")
list(APPEND CMAKE_PREFIX_PATH ${BUILD_DIR})

#set(MONO_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_subdirectory(${AIM_ROOT}/lib/pybind11 pybind11)

set(IMGUI_HEADERS
    ${IMGUI_ROOT}/imconfig.h
    ${IMGUI_ROOT}/imgui_internal.h
    ${IMGUI_ROOT}/imgui.h
    ${IMGUI_ROOT}/imstb_rectpack.h
    ${IMGUI_ROOT}/imstb_textedit.h
    ${IMGUI_ROOT}/imstb_truetype.h
)
set(IMGUI_ROOT ${AIM_ROOT}/lib/imgui)

set(AIMGUI_ROOT ${AIMROOT}/pkg/aimgui)

#list(APPEND CMAKE_MODULE_PATH "${AIMGUI_ROOT}/cmake")

include(${CMAKE_CURRENT_LIST_DIR}/Functions.cmake)