# AimGui :anger:

AimGui is a library that extends and wraps [Dear ImGui](https://github.com/ocornut/imgui) for use with Python Game Libraries

:package: [Package](https://pypi.org/project/aimgui/)

## Game Libraries Supported

[The Python Arcade Library](https://arcade.academy/)

## Prerequisites

Get [Poetry](https://python-poetry.org/)
Ninja
CMake

## Clone

Clone the repository and change directory

       git clone https://github.com/kfields/aimgui.git
       cd aimgui

## Run the Demo

        cd imdemo
        poetry install
        poetry shell
        python imdemo

### Individual Examples

        python examples/bullet.py
        python examples/colors.py
        etc ...

## Run the ImFlo Demo

        cd imflo
        poetry install
        poetry shell
        python imdemo


# Development

## Tool Chain

[Binder](https://github.com/RosettaCommons/binder)

[pybind11](https://github.com/pybind/pybind11)

[scikit-build](https://github.com/scikit-build/scikit-build)

## Build

        python setup.py build --build-type Debug

## Building Binder
        sudo apt install python3-pybind11
        cd extern/binder
        cmake CMakeLists.txt -DCMAKE_INSTALL_PREFIX:PATH=$HOME/.local
        make
        make install

        binder --root-module imgui --prefix bindings \
        --bind ImGui \
        imgui_root.hpp \
        -- -std=c++11 -Iextern

        binder --root-module aimgui --prefix bindings \
        --bind ImGui \
        imgui_root.hpp \
        -- -std=c++11 -Iextern
