cmake_minimum_required(VERSION 3.4)

project(aimnodes VERSION "0.1")

set(THIS ${PROJECT_NAME})

include(../../cmake/ImGui.cmake)

set(IMNODES_ROOT ${AIM_ROOT}/lib/imnodes)

set(IMNODES_HEADERS
    ${IMNODES_ROOT}/imnodes.h
    ${IMNODES_ROOT}/imnodes_internal.h
    src/aimnodes/aimnodes_config.h
)

set(IMNODES_SRC
    src/aimnodes/bindings/generated.cpp
    src/aimnodes/bindings/main.cpp
    ${IMNODES_ROOT}/imnodes.cpp
)

pybind11_add_module(aimnodes MODULE
    src/aimnodes/bindings/init.cpp
)
USES_IMGUI(${THIS})
configure_project(${THIS})

target_compile_definitions(${THIS} PRIVATE IMNODES_USER_CONFIG=<aimnodes/aimnodes_config.h>)

install(TARGETS aimnodes EXPORT AimNodesTargets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
target_sources(${THIS} PRIVATE ${IMNODES_SRC} ${IMNODES_HEADERS})

# add include files
target_sources(${THIS} PRIVATE ${AIMNODES_INCLUDE}) # for intellisense
target_include_directories(${THIS}
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_ROOT}/include>
        $<BUILD_INTERFACE:${IMGUI_ROOT}>
        $<BUILD_INTERFACE:${IMNODES_ROOT}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

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