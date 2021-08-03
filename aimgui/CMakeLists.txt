cmake_minimum_required(VERSION 3.4)

project(aimgui VERSION "0.1")

include(../cmake/Common.cmake)

set(IMGUI_SRC
    src/aimgui/bindings/generated.cpp
    src/aimgui/bindings/main.cpp
    ${IMGUI_DIR}/imgui_demo.cpp
    ${IMGUI_DIR}/imgui_draw.cpp
    ${IMGUI_DIR}/imgui_tables.cpp
    ${IMGUI_DIR}/imgui_widgets.cpp
    ${IMGUI_DIR}/imgui.cpp
)

pybind11_add_module(aimgui SHARED
    src/aimgui/bindings/init.cpp
)

configure_project(aimgui)

add_compile_definitions(AIMGUI_DLL)

install(TARGETS aimgui EXPORT AimGuiTargets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimgui PRIVATE ${IMGUI_SRC} ${IMGUI_HEADERS})

# add include files
target_sources(aimgui PRIVATE ${AIMGUI_INCLUDE}) # for intellisense
target_include_directories(aimgui
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)
#
# INSTALL
#
# install headers
install(FILES ${IMGUI_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


install(TARGETS aimgui DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimgui
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimgui.so ./
#)

#
# Generate a configuration for use by plugins
#
message(Build ${BUILD_DIR})
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
  "${BUILD_DIR}/aimgui/AimGuiConfigVersion.cmake"
  VERSION ${Upstream_VERSION}
  COMPATIBILITY AnyNewerVersion
)

export(EXPORT AimGuiTargets
  FILE "${BUILD_DIR}/aimgui/AimGuiTargets.cmake"
  NAMESPACE Upstream::
)
configure_file(cmake_config/AimGuiConfig.cmake
  "${BUILD_DIR}/aimgui/AimGuiConfig.cmake"
  COPYONLY
)

set(ConfigPackageLocation lib/cmake/AimGui)
install(EXPORT AimGuiTargets
  FILE
  AimGuiTargets.cmake
  NAMESPACE
    Upstream::
  DESTINATION
    ${ConfigPackageLocation}
)
install(
  FILES
    cmake_config/AimGuiConfig.cmake
    "${BUILD_DIR}/aimgui/AimGuiConfig.cmake"
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Devel
)