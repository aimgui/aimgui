cmake_minimum_required(VERSION 3.4)

project(aimgui VERSION "0.1")

set(THIS ${PROJECT_NAME})

include(../../cmake/Common.cmake)

set(IMGUI_SRC
    src/aimgui/bindings/generated.cpp
    src/aimgui/bindings/main.cpp
    ${IMGUI_ROOT}/imgui_demo.cpp
    ${IMGUI_ROOT}/imgui_draw.cpp
    ${IMGUI_ROOT}/imgui_tables.cpp
    ${IMGUI_ROOT}/imgui_widgets.cpp
    ${IMGUI_ROOT}/imgui.cpp
)

pybind11_add_module(aimgui SHARED
    src/aimgui/bindings/init.cpp
)

configure_project(${THIS})
USES_STANDARD(${THIS})

#set_target_properties(${THIS}
#    PROPERTIES
#        LIBRARY_OUTPUT_DIRECTORY ${AIM_ROOT}/pkg/aimgui/aimgui
#        RUNTIME_OUTPUT_DIRECTORY ${AIM_ROOT}/pkg/aimgui/aimgui
#)

install(TARGETS ${THIS}
  COMPONENT python
  LIBRARY DESTINATION "${AIM_ROOT}/pkg/aimgui/aimgui"
  )

target_compile_definitions(aimgui PRIVATE AIMGUI_DLL IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)

target_sources(aimgui PRIVATE ${IMGUI_SRC} ${IMGUI_HEADERS})

# add include files
target_sources(aimgui PRIVATE ${AIMGUI_INCLUDE}) # for intellisense
target_include_directories(aimgui
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_ROOT}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)
#
# INSTALL
#
# install headers
install(FILES ${IMGUI_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


install(TARGETS aimgui LIBRARY DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

get_target_property(_RUNTIME_OUTPUT_DIRECTORY ${THIS} RUNTIME_OUTPUT_DIRECTORY)

add_custom_command(
        TARGET ${THIS} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
                ${_RUNTIME_OUTPUT_DIRECTORY}/Debug/_aimgui.pyd
                ${CMAKE_CURRENT_SOURCE_DIR}/aimgui/_aimgui.pyd
                )
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

#export(EXPORT AimGuiTargets
#  FILE "${BUILD_DIR}/aimgui/AimGuiTargets.cmake"
#  NAMESPACE Upstream::
#)

configure_file(cmake_config/AimGuiConfig.cmake
  "${BUILD_DIR}/aimgui/AimGuiConfig.cmake"
  COPYONLY
)

set(ConfigPackageLocation lib/cmake/AimGui)
#install(EXPORT AimGuiTargets
#  FILE
#  AimGuiTargets.cmake
#  NAMESPACE
#    Upstream::
#  DESTINATION
#    ${ConfigPackageLocation}
#)

install(
  FILES
    cmake_config/AimGuiConfig.cmake
    "${BUILD_DIR}/aimgui/AimGuiConfig.cmake"
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Devel
)