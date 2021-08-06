cmake_minimum_required(VERSION 3.4)

project(aimgfx VERSION "0.1")

include(../cmake/Common.cmake)

#find_package(AimGui REQUIRED)

set(BX_DIR ${MONO_DIR}/bx)

set(BIMG_DIR ${MONO_DIR}/bimg)

set(BGFX_DIR ${MONO_DIR}/bgfx)

set(BGFX_HEADERS
    ${BGFX_DIR}/include/bgfx/bgfx.h
)

set(BGFX_SRC
    src/aimgfx/bindings/generated.cpp
    src/aimgfx/bindings/main.cpp
    ${BGFX_DIR}/src/amalgamated.cpp
)

pybind11_add_module(aimgfx MODULE
    src/aimgfx/bindings/init.cpp
)

configure_project(${PROJECT_NAME})

install(TARGETS aimgfx EXPORT aimgfx-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
target_compile_definitions(aimgfx PRIVATE IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)
#target_compile_definitions(aimgfx PRIVATE IMGUI_API=PYBIND11_EXPORT)
target_sources(aimgfx PRIVATE ${BGFX_SRC} ${BGFX_HEADERS})

# add include files
target_sources(aimgfx PRIVATE ${AIMGFX_INCLUDE}) # for intellisense
target_include_directories(aimgfx
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${BGFX_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${BGFX_DIR}/include
        ${BX_DIR}/include
        ${BX_DIR}/include/compat/msvc
        ${BIMG_DIR}/include
        ${BGFX_DIR}/3rdparty
        ${BGFX_DIR}/3rdparty/khronos
        ${BGFX_DIR}/3rdparty/dxsdk/include
)

#target_link_libraries(aimgfx PRIVATE Upstream::aimgui)

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${BGFX_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimgfx DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimgfx
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimgfx.so ./
#)