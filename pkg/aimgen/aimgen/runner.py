import os, sys

from pathlib import Path
import importlib.util

from clang import cindex

from . import generator as __aimgen__

class Runner:
    def __init__(self):
        if sys.platform == 'darwin':
            cindex.Config.set_library_path('/usr/local/opt/llvm@6/lib')
        elif sys.platform == 'linux':
            cindex.Config.set_library_file('libclang-10.so')
        else:
            cindex.Config.set_library_file('C:/Program Files/LLVM/bin/libclang.dll')
            #cindex.Config.set_library_path('C:/Program Files/LLVM/bin')

    def gen(self, name):
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

    def gen_all(self):
        path = Path(os.getcwd(), '__aimgen__')
        files = path.glob('*.toml')
        for file in files:
            self.gen(file.stem)