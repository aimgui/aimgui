cmake_minimum_required(VERSION 3.4)

set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

add_subdirectory(pkg/aimgui)
add_subdirectory(pkg/aimgfx)
add_subdirectory(pkg/aimnodes)
add_subdirectory(pkg/aimplot)
