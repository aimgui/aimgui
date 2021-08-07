import os

from pathlib import Path

import importlib.util

from . import generator as __aimgen__

def main(name):
    '''
    if __init__.py exists in projects __aimgen__ directory
    then create custom generator
    else use base generator
    '''
    global __aimgen__
    path = Path(os.getcwd(), '__aimgen__', '__init__.py')
    if os.path.exists(path):
        spec = importlib.util.spec_from_file_location(
            "__aimgen__", path
        )
        __aimgen__ = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(__aimgen__)

    generator = __aimgen__.Generator.create(name)
    generator.generate()
