cmake_minimum_required(VERSION 3.4)

project(aimgfx VERSION "0.1")

include(../cmake/Common.cmake)

#find_package(AimGui REQUIRED)
set(AIMGFX_DIR ${CMAKE_CURRENT_SOURCE_DIR})

set(BX_DIR ${MONO_DIR}/bx)
set(BX_SRC
  ${BX_DIR}/src/amalgamated.cpp
)
set(BIMG_DIR ${MONO_DIR}/bimg)

set(OPTION_ASTC_TESTS OFF CACHE BOOL "Build all the unit tests" FORCE)
add_subdirectory(${BIMG_DIR}/3rdparty/astc-codec astc-codec)

set(BIMG_SRC
  ${BIMG_DIR}/src/image.cpp
  ${BIMG_DIR}/src/image_gnf.cpp
)

set(BGFX_DIR ${MONO_DIR}/bgfx)

set(BGFX_HEADERS
    ${BGFX_DIR}/include/bgfx/bgfx.h
)

set(BGFX_SRC
    ${BGFX_DIR}/src/amalgamated.cpp
)

set(AIMGFX_HEADERS
    ${AIMGFX_DIR}/include/aimgfx/aimgfx.h
)

set(AIMGFX_SRC
    src/aimgfx/bindings/bgfx.cpp
    src/aimgfx/bindings/platform.cpp
    src/aimgfx/bindings/embedded_shader.cpp
    src/aimgfx/bindings/main.cpp
)

pybind11_add_module(aimgfx MODULE
    src/aimgfx/bindings/init.cpp
)

configure_project(${PROJECT_NAME})

install(TARGETS aimgfx EXPORT aimgfx-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
#TODO:PRIxPTR???
target_compile_definitions(aimgfx PRIVATE PRIxPTR="Ix")
target_sources(aimgfx PRIVATE
    ${AIMGFX_SRC} ${AIMGFX_HEADERS}
    ${BGFX_SRC} ${BGFX_HEADERS}
    ${BX_SRC} ${BIMG_SRC}
)

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
        ${BX_DIR}/include/compat/msvc
        ${BX_DIR}/include
        ${BX_DIR}/3rdparty
        ${BIMG_DIR}/include
        ${BIMG_DIR}/3rdparty
        #${BIMG_DIR}/3rdparty/astc-codec/include
        #${BIMG_DIR}/3rdparty/astc-codec
        ${BGFX_DIR}/include
        ${BGFX_DIR}/3rdparty
        ${BGFX_DIR}/3rdparty/khronos
        ${BGFX_DIR}/3rdparty/dxsdk/include
)

#target_link_libraries(aimgfx PRIVATE Upstream::aimgui)
target_link_libraries(aimgfx PRIVATE astc-codec)

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