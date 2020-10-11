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

        cd aimdemo
        poetry install
        poetry shell
        python aimdemo

### Individual Examples

        python examples/basic.py
        etc ...

## Run the AimFlo Demo

        cd aimflo
        poetry install
        poetry shell
        python aimflo


# Development

## Tool Chain

[pybind11](https://github.com/pybind/pybind11)

[scikit-build](https://github.com/scikit-build/scikit-build)

## Build

        python setup.py build --build-type Debug
