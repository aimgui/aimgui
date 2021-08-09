cmake_minimum_required(VERSION 3.14)

include(${MONO_DIR}/cmake/ImGui.cmake)

project(AimShell LANGUAGES CXX)
set(THIS ${PROJECT_NAME})


file(GLOB SHELL_SRC ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
file(GLOB SHELL_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

add_library(${THIS} STATIC
  ${SHELL_SRC}
  ${SHELL_INCLUDE}
)
USES_IMGUI(${THIS})

target_link_libraries(${THIS} ${PROJECT_NAME}${CMAKE_SYSTEM_NAME} glfw)

target_include_directories(${THIS} PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/../
)
add_subdirectory(platform/windows)
