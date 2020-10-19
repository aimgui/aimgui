cmake_minimum_required(VERSION 3.14...3.17)

# This is from scikit-build
find_package(PythonExtensions REQUIRED)

SET(CMAKE_CXX_FLAGS  "-Wno-format-security")

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

project(aimgui VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

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

set(IMGUI_SRC
    src/aimgui/bindings/generated.cpp
    src/aimgui/bindings/main.cpp
    ${IMGUI_DIR}/imgui_demo.cpp
    ${IMGUI_DIR}/imgui_draw.cpp
    ${IMGUI_DIR}/imgui_widgets.cpp
    ${IMGUI_DIR}/imgui.cpp
)

#pybind11_add_module(aimgui MODULE
pybind11_add_module(aimgui SHARED
    src/aimgui/bindings/init.cpp
)

set_target_properties(aimgui PROPERTIES PREFIX "lib")
set_target_properties(aimgui PROPERTIES SUFFIX ".so")

install(TARGETS aimgui EXPORT AimGuiTargets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimgui PRIVATE ${IMGUI_SRC} ${IMGUI_HEADERS})
#target_sources(aimgui PRIVATE ${IMPLOT_SRC} ${IMPLOT_HEADERS})

# add include files
target_sources(aimgui PRIVATE ${AIMGUI_INCLUDE}) # for intellisense
target_include_directories(aimgui
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        # $<BUILD_INTERFACE:${IMPLOT_INCLUDE_DIR}>
        # $<BUILD_INTERFACE:${NANOSVG_INCLUDE_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)
#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${IMGUI_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
#install(FILES ${IMPLOT_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimgui DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimgui
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimgui.so ./
#)

#
# Generate a configuration for use by plugins
#

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/aimgui/AimGuiConfigVersion.cmake"
  VERSION ${Upstream_VERSION}
  COMPATIBILITY AnyNewerVersion
)

export(EXPORT AimGuiTargets
  FILE "${CMAKE_CURRENT_BINARY_DIR}/aimgui/AimGuiTargets.cmake"
  NAMESPACE Upstream::
)
configure_file(cmake/AimGuiConfig.cmake
  "${CMAKE_CURRENT_BINARY_DIR}/aimgui/AimGuiConfig.cmake"
  COPYONLY
)

set(ConfigPackageLocation lib/cmake/AimGui)
install(EXPORT AimGuiTargets
  FILE
  AimGuiTargets.cmake
  NAMESPACE
    Upstream::
  DESTINATION
    ${ConfigPackageLocation}
)
install(
  FILES
    cmake/AimGuiConfig.cmake
    "${CMAKE_CURRENT_BINARY_DIR}/aimgui/AimGuiConfig.cmake"
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Devel
)