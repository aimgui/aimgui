# AimGui :anger:

AimGui is a library that extends and wraps [Dear ImGui](https://github.com/ocornut/imgui) for use with Python Game Libraries

:package: [Package](https://pypi.org/project/aimgui/)

## Game Libraries Supported

[The Python Arcade Library](https://arcade.academy/)

## Prerequisites

* [Poetry](https://python-poetry.org/)
* CMake
* Ninja (Optional)

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

[deargui](https://github.com/cammm/deargui)

[pyimgui](https://github.com/swistakm/pyimgui)