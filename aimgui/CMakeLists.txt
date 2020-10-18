cmake_minimum_required(VERSION 3.14...3.17)

SET(CMAKE_CXX_FLAGS  "-Wno-format-security")

add_compile_definitions(IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

project(aimgui VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

add_subdirectory(extern/pybind11)

# IMGUI
set(IMGUI_HEADERS
    extern/imgui/imconfig.h
    extern/imgui/imgui_internal.h
    extern/imgui/imgui.h
    extern/imgui/imstb_rectpack.h
    extern/imgui/imstb_textedit.h
    extern/imgui/imstb_truetype.h
)

set(IMGUI_SRC
    src/aimgui/bindings/generated.cpp
    src/aimgui/bindings/main.cpp
    extern/imgui/imgui_demo.cpp
    extern/imgui/imgui_draw.cpp
    extern/imgui/imgui_widgets.cpp
    extern/imgui/imgui.cpp
)

set(IMGUI_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/extern/imgui)

pybind11_add_module(aimgui MODULE
    src/aimgui/bindings/init.cpp
)

set_target_properties(aimgui PROPERTIES PREFIX "lib")
set_target_properties(aimgui PROPERTIES SUFFIX ".so")

install(TARGETS aimgui EXPORT aimgui-targets
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
        $<BUILD_INTERFACE:${IMGUI_INCLUDE_DIR}>
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