cmake_minimum_required(VERSION 3.4)

project(aimplot VERSION "0.1")

set(THIS ${PROJECT_NAME})

include(../../cmake/ImGui.cmake)

set(IMPLOT_ROOT ${AIM_ROOT}/lib/implot)

set(IMPLOT_HEADERS
    ${IMPLOT_ROOT}/implot.h
    ${IMPLOT_ROOT}/implot_internal.h
)

set(IMPLOT_SRC
    src/aimplot/bindings/generated.cpp
    src/aimplot/bindings/main.cpp
    ${IMPLOT_ROOT}/implot_demo.cpp
    ${IMPLOT_ROOT}/implot_items.cpp
    ${IMPLOT_ROOT}/implot.cpp
)

pybind11_add_module(${THIS} MODULE
    src/aimplot/bindings/init.cpp
)
USES_IMGUI(${THIS})
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
        $<BUILD_INTERFACE:${AIMGUI_ROOT}/include>
        $<BUILD_INTERFACE:${IMGUI_ROOT}>
        $<BUILD_INTERFACE:${IMPLOT_ROOT}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

#target_link_libraries(aimplot PRIVATE Upstream::aimgui)

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