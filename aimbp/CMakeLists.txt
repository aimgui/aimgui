cmake_minimum_required(VERSION 3.14...3.17)

# This is from scikit-build
find_package(PythonExtensions REQUIRED)

SET(CMAKE_CXX_FLAGS  "-Wno-format-security")

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

project(aimbp VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

set(MONO_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

set(AIMGUI_DIR ${MONO_DIR}/aimgui)
set(AimGui_DIR ${MONO_DIR}/aimgui/cmake)
set(IMGUI_DIR ${MONO_DIR}/imgui)
set(IMBP_DIR ${MONO_DIR}/imbp)

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

set(IMBP_HEADERS
    ${IMBP_DIR}/imgui_node_editor.h
    ${IMBP_DIR}/imgui_node_editor_internal.h
)

set(IMBP_SRC
    src/aimbp/bindings/generated.cpp
    src/aimbp/bindings/main.cpp
    ${IMBP_DIR}/imgui_node_editor.cpp
    ${IMBP_DIR}/imgui_node_editor_api.cpp
    ${IMBP_DIR}/crude_json.cpp
    ${IMBP_DIR}/imgui_canvas.cpp
)

pybind11_add_module(aimbp MODULE
    src/aimbp/bindings/init.cpp
)

set_target_properties(aimbp PROPERTIES PREFIX "lib")
set_target_properties(aimbp PROPERTIES SUFFIX ".so")

install(TARGETS aimbp EXPORT aimbp-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimbp PRIVATE ${IMBP_SRC} ${IMBP_HEADERS})

# add include files
target_sources(aimbp PRIVATE ${AIMBP_INCLUDE}) # for intellisense
target_include_directories(aimbp
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${IMBP_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

#target_link_libraries(aimbp PRIVATE pybind11::module aimgui)

# scikit-build:  conflicting with pybind11
#target_link_libraries_with_dynamic_lookup(aimbp PRIVATE pybind11::module aimgui)

target_link_libraries(aimbp PRIVATE ${AimGuiTargets})

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${IMBP_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimbp DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimbp
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimbp.so ./
#)