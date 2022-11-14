# AimGui :anger:

AimGui is a library that extends and wraps [Dear ImGui](https://github.com/ocornut/imgui) for use with Python OpenGL Libraries

<!-- :package: [Package](https://pypi.org/project/aimgui/) -->

:warning:  This is pre-alpha software.  Do not use it for production.  Packages and binary wheels are a work in progress

## Motivation

I wanted to experiment with the latest features of Dear ImGui's docking branch.
My first thought was to fork [pyimgui](https://github.com/swistakm/pyimgui) but I am not familiar with ctypes so I chose a different route.
I combined the Python parts of pyimgui with the C++ parts of [deargui](https://github.com/cammm/deargui), another excellent project

## OpenGL Libraries Supported

[The Python Arcade Library](https://arcade.academy)

[ModernGL](https://github.com/moderngl/moderngl)

## Required

* [Poetry](https://python-poetry.org/)

## Optional

* [Ninja](https://ninja-build.org/)

## Clone

        git clone --recursive https://github.com/aimgui/aimgui
        cd aimgui

## Virtual Environment

        poetry shell

## Build AimGui

        cd aimgui
        poetry install
        python setup.py build

### Or

        python setup.py build --build-type Debug

### Visual Studio 2019
        python setup.py build -G "Visual Studio 16 2019" --build-type Debug
        python setup.py build -G "Visual Studio 17 2022" --build-type Debug

## Run the Demo

        cd aimdemo
        poetry install
        python aimdemo

### Individual Examples

        python examples/basic.py
        etc ...

## Build AimPlot

        cd aimplot
        poetry install
        python setup.py build

## Run the Demo

        cd aimplotdemo
        poetry install
        python aimplotdemo

## Run the AimFlo Demo

        cd aimflo
        poetry install
        python aimflo

# Development

## Tool Chain

[scikit-build](https://github.com/scikit-build/scikit-build)

[pybind11](https://github.com/pybind/pybind11)

## Build

### Generate Bindings

        aimgen gen

### Release

        python setup.py build

### Debug

        python setup.py build --build-type Debug

# Attribution

I'd like to thank the authors of the following repositories for making this possible!

[pyimgui](https://github.com/swistakm/pyimgui)

[deargui](https://github.com/cammm/deargui)