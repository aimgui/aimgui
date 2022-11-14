include_guard()

# Standard includes
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)
include(CMakeDependentOption)

set(AIM_ROOT ${CMAKE_CURRENT_LIST_DIR}/..)
set(PYBIND11_ROOT ${AIM_ROOT}/lib/pybind11)
set(IMGUI_ROOT ${AIM_ROOT}/lib/imgui)
set(IMPLOT_ROOT ${AIM_ROOT}/lib/implot)
set(IMNODES_ROOT ${AIM_ROOT}/lib/imnodes)
