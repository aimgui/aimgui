cmake_minimum_required(VERSION 3.14...3.17)

# This is from scikit-build
find_package(PythonExtensions REQUIRED)

SET(CMAKE_CXX_FLAGS  "-Wno-format-security")

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

project(aimnodes VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

set(MONO_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

set(AIMGUI_DIR ${MONO_DIR}/aimgui)
set(AimGui_DIR ${MONO_DIR}/aimgui/cmake)
set(IMGUI_DIR ${MONO_DIR}/imgui)
set(IMNODES_DIR ${MONO_DIR}/imnodes)

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

set(IMNODES_HEADERS
    ${IMNODES_DIR}/imnodes.h
)

set(IMNODES_SRC
    src/aimnodes/bindings/generated.cpp
    src/aimnodes/bindings/main.cpp
    ${IMNODES_DIR}/imnodes.cpp
)

pybind11_add_module(aimnodes MODULE
    src/aimnodes/bindings/init.cpp
)

set_target_properties(aimnodes PROPERTIES PREFIX "lib")
set_target_properties(aimnodes PROPERTIES SUFFIX ".so")

install(TARGETS aimnodes EXPORT aimnodes-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimnodes PRIVATE ${IMNODES_SRC} ${IMNODES_HEADERS})

# add include files
target_sources(aimnodes PRIVATE ${AIMNODES_INCLUDE}) # for intellisense
target_include_directories(aimnodes
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${IMNODES_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

#target_link_libraries(aimnodes PRIVATE pybind11::module aimgui)

# scikit-build:  conflicting with pybind11
#target_link_libraries_with_dynamic_lookup(aimnodes PRIVATE pybind11::module aimgui)

target_link_libraries(aimnodes PRIVATE ${AimGuiTargets})

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${IMNODES_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimnodes DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimnodes
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimnodes.so ./
#)