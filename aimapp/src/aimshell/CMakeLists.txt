cmake_minimum_required(VERSION 3.14)

project(AimShell LANGUAGES CXX)
set(THIS ${PROJECT_NAME})

include(${AIM_ROOT}/cmake/AIM.cmake)
include(${AIM_ROOT}/cmake/ImGui.cmake)

file(GLOB SHELL_SRC ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
file(GLOB SHELL_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

add_library(${THIS} STATIC
  ${SHELL_SRC}
  ${SHELL_INCLUDE}
)
USES_AIM(${THIS})
USES_IMGUI(${THIS})
target_link_libraries(${THIS} ${PROJECT_NAME}${CMAKE_SYSTEM_NAME} glfw)

add_subdirectory(platform/windows)
