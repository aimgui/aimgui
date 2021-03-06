cmake_minimum_required(VERSION 3.14...3.17)

# This is from scikit-build
find_package(PythonExtensions REQUIRED)

SET(CMAKE_CXX_FLAGS  "-Wno-format-security")

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

project(aimplot VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

set(MONO_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

set(AIMGUI_DIR ${MONO_DIR}/aimgui)
set(AimGui_DIR ${MONO_DIR}/aimgui/cmake)
set(IMGUI_DIR ${MONO_DIR}/imgui)
set(IMPLOT_DIR ${MONO_DIR}/implot)

list(APPEND CMAKE_MODULE_PATH "${AIMGUI_DIR}/cmake")
find_package(AimGui REQUIRED)

add_subdirectory(${MONO_DIR}/pybind11 build)

set(IMGUI_HEADERS
    ${IMGUI_DIR}/imconfig.h
    ${IMGUI_DIR}/imgui_internal.h
    ${IMGUI_DIR}/imgui.h
    ${IMGUI_DIR}/imstb_rectpack.h
    ${IMGUI_DIR}/imstb_textedit.h
    ${IMGUI_DIR}/imstb_truetype.h
)

set(IMPLOT_HEADERS
    ${IMPLOT_DIR}/implot.h
    ${IMPLOT_DIR}/implot_internal.h
    ${IMPLOT_DIR}/implot.h
)

set(IMPLOT_SRC
    src/aimplot/bindings/generated.cpp
    src/aimplot/bindings/main.cpp
    ${IMPLOT_DIR}/implot_demo.cpp
    ${IMPLOT_DIR}/implot_items.cpp
    ${IMPLOT_DIR}/implot.cpp
)

pybind11_add_module(aimplot MODULE
    src/aimplot/bindings/init.cpp
)

set_target_properties(aimplot PROPERTIES PREFIX "lib")
set_target_properties(aimplot PROPERTIES SUFFIX ".so")

install(TARGETS aimplot EXPORT aimplot-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimplot PRIVATE ${IMPLOT_SRC} ${IMPLOT_HEADERS})

# add include files
target_sources(aimplot PRIVATE ${AIMPLOT_INCLUDE}) # for intellisense
target_include_directories(aimplot
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${IMPLOT_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

#target_link_libraries(aimplot PRIVATE pybind11::module aimgui)

# scikit-build:  conflicting with pybind11
#target_link_libraries_with_dynamic_lookup(aimplot PRIVATE pybind11::module aimgui)

target_link_libraries(aimplot PRIVATE ${AimGuiTargets})

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${IMPLOT_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimplot DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimplot
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimplot.so ./
#)