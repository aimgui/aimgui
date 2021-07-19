cmake_minimum_required(VERSION 3.4)

project(aimplot VERSION "0.1")

include(../cmake/Common.cmake)

find_package(AimGui REQUIRED)

set(IMPLOT_DIR ${MONO_DIR}/implot)

set(IMPLOT_HEADERS
    ${IMPLOT_DIR}/implot.h
    ${IMPLOT_DIR}/implot_internal.h
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

configure_project(${PROJECT_NAME})

install(TARGETS aimplot EXPORT AimPlotTargets
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

target_link_libraries(aimplot PRIVATE Upstream::aimgui)

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