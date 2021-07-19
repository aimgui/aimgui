cmake_minimum_required(VERSION 3.4)

project(aimbp VERSION "0.1")

include(../cmake/Common.cmake)

find_package(AimGui REQUIRED)

set(IMBP_DIR ${MONO_DIR}/imbp)

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

target_link_libraries(aimbp PRIVATE Upstream::aimgui)

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