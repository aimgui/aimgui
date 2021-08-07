import os
import sys

from pathlib import Path

import importlib.util

def main(name):
    path = Path(os.getcwd(), '__aimgen__', '__init__.py')
    spec = importlib.util.spec_from_file_location(
        "__aimgen__", path
    )
    __aimgen__ = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(__aimgen__)

    generator = __aimgen__.Generator.create(name)
    generator.generate()
