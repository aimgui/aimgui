cmake_minimum_required(VERSION 3.4)

project(aimgfx VERSION "0.1")

set(THIS ${PROJECT_NAME})

include(../../cmake/Aim.cmake)

set(AIMGFX_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

set(BX_ROOT ${AIM_ROOT}/lib/bx)
set(BX_SRC
  ${BX_ROOT}/src/amalgamated.cpp
)
set(BIMG_ROOT ${AIM_ROOT}/lib/bimg)

set(OPTION_ASTC_TESTS OFF CACHE BOOL "Build all the unit tests" FORCE)
#add_subdirectory(${BIMG_ROOT}/3rdparty/astc-codec astc-codec)
add_subdirectory(${AIM_ROOT}/src/bimg)

set(BIMG_SRC
  ${BIMG_ROOT}/src/image.cpp
  ${BIMG_ROOT}/src/image_gnf.cpp
)

set(BGFX_ROOT ${AIM_ROOT}/lib/bgfx)

set(BGFX_HEADERS
    ${BGFX_ROOT}/include/bgfx/bgfx.h
)

set(BGFX_SRC
    ${BGFX_ROOT}/src/amalgamated.cpp
)

set(AIMGFX_HEADERS
    ${AIMGFX_ROOT}/include/aimgfx/aimgfx.h
)

set(AIMGFX_SRC
    src/aimgfx/bindings/bgfx.cpp
    src/aimgfx/bindings/platform.cpp
    src/aimgfx/bindings/embedded_shader.cpp
    src/aimgfx/bindings/main.cpp
)

pybind11_add_module(${THIS} SHARED
    src/aimgfx/bindings/init.cpp
)
USES_AIM(${THIS})
configure_project(${PROJECT_NAME})

install(TARGETS ${THIS} EXPORT AimGfxTargets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
#TODO:PRIxPTR???
target_compile_definitions(aimgfx PRIVATE PRIxPTR="Ix")
target_sources(${THIS} PRIVATE
    ${AIMGFX_SRC} ${AIMGFX_HEADERS}
    ${BGFX_SRC} ${BGFX_HEADERS}
    ${BX_SRC} ${BIMG_SRC}
)

# add include files
target_sources(${THIS} PRIVATE ${AIMGFX_INCLUDE}) # for intellisense
target_include_directories(${THIS}
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${BGFX_ROOT}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${BX_ROOT}/include/compat/msvc
        ${BX_ROOT}/include
        ${BX_ROOT}/3rdparty
        ${BIMG_ROOT}/include
        ${BIMG_ROOT}/3rdparty
        #${BIMG_ROOT}/3rdparty/astc-codec/include
        #${BIMG_ROOT}/3rdparty/astc-codec
        ${BGFX_ROOT}/include
        ${BGFX_ROOT}/3rdparty
        ${BGFX_ROOT}/3rdparty/khronos
        ${BGFX_ROOT}/3rdparty/dxsdk/include
)

target_link_libraries(${THIS} PRIVATE astc-codec)

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

#
# Generate a configuration for use by plugins
#
message(Build ${BUILD_DIR})
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  "${BUILD_DIR}/aimgfx/AimGfxConfigVersion.cmake"
  VERSION ${Upstream_VERSION}
  COMPATIBILITY AnyNewerVersion
)

export(EXPORT AimGfxTargets
  FILE "${BUILD_DIR}/aimgfx/AimGfxTargets.cmake"
  NAMESPACE Upstream::
)
configure_file(cmake_config/AimGfxConfig.cmake
  "${BUILD_DIR}/aimgfx/AimGfxConfig.cmake"
  COPYONLY
)

set(ConfigPackageLocation lib/cmake/AimGfx)
install(EXPORT AimGfxTargets
  FILE
  AimGfxTargets.cmake
  NAMESPACE
    Upstream::
  DESTINATION
    ${ConfigPackageLocation}
)
install(
  FILES
    cmake_config/AimGfxConfig.cmake
    "${BUILD_DIR}/aimgfx/AimGfxConfig.cmake"
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Devel
)