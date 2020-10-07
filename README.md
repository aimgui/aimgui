# AimGui :anger:

AimGui is a library that extends and wraps [Dear ImGui](https://github.com/ocornut/imgui) for use with Python Game Libraries

:package: [Package](https://pypi.org/project/aimgui/)

## Game Libraries Supported

[The Python Arcade Library](https://arcade.academy/)

## Tool Chain

[Binder](https://github.com/RosettaCommons/binder)

[pybind11](https://github.com/pybind/pybind11)

[scikit-build](https://github.com/scikit-build/scikit-build)

## Prerequisite

Get [Poetry](https://python-poetry.org/)

## Clone

Clone the repository and change directory

       git clone https://github.com/kfields/arcade-imgui.git
       cd arcade-imgui

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
        python setup.py build --build-type Debug