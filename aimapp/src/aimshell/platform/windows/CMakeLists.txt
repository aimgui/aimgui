cmake_minimum_required(VERSION 3.14)

set(THIS ${PROJECT_NAME}${CMAKE_SYSTEM_NAME})

include(${FAUSTY_ROOT}/cmake/Fausty.cmake)
include(${FAUSTY_ROOT}/cmake/ImGui.cmake)

file(GLOB SHELL_SRC ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
file(GLOB SHELL_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

add_library(${THIS} STATIC
  ${SHELL_SRC}
  ${SHELL_INCLUDE}

  ${IMGUI_EX}/imgui_impl_dx12.cpp
)
USES_FAUSTY(${THIS})
USES_IMGUI(${THIS})

if(${SHELL_BACKEND} STREQUAL "Gl3")
  add_subdirectory(gl3)
elseif(${SHELL_BACKEND} STREQUAL "Dx12")
  add_subdirectory(dx12)
endif()

