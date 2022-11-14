cmake_minimum_required(VERSION 3.4)

set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

#
# pybind11
#
set(-DCMAKE_CXX_STANDARD=20 -std=c++20)
set(PYBIND11_PYTHON_VERSION 3.10)

#if(${HAS_PYBIND11})
add_subdirectory(lib/pybind11)
#endif() #HAS_PYBIND11

add_subdirectory(pkg/aimgui)
add_subdirectory(pkg/aimnodes)
add_subdirectory(pkg/aimplot)
