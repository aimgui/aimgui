import os
import re
import sys
from pathlib import Path

from clang import cindex

from . import UserSet

from .parser import Parser

import importlib

import jinja2

def snakecase(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Options:
    def __init__(self, *options, **kwargs):
        for dictionary in options:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class Overloaded(UserSet):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.visited = set()

    def is_overloaded(self, node):
        return self.name(node) in self

class GeneratorBase(Parser):
    def __init__(self, config, **kwargs):
        super().__init__()
        self.config = config
        self.options = { 'save': True }
        for key in config:
            setattr(self, key, config[key])
        for key in kwargs:
            if key == 'options':
                options = kwargs[key]
                options.update(self.options)
                self.options = options

            setattr(self, key, kwargs[key])
        
        self.options = Options(self.options)
        self.overloaded = Overloaded(self.overloaded)

        BASE_PATH = Path('.')
        self.path = BASE_PATH / self.source


    def import_factories(self):
        #path = Path(os.getcwd(), '__aimgen__', '__init__.py')
        path = Path(os.path.dirname(os.path.abspath(__file__)), 'factories.py')
        spec = importlib.util.spec_from_file_location(
            "factories", path
        )
        __factories__ = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(__factories__)

        self.factories = __factories__.MAP

    @property
    def header(self):
        pass

    @property
    def footer(self):
        pass

    @property
    def defaults(self):
        pass

    def generate(self):
        if sys.platform == 'darwin':
            cindex.Config.set_library_path('/usr/local/opt/llvm@6/lib')
        elif sys.platform == 'linux':
            cindex.Config.set_library_file('libclang-10.so')
        else:
            cindex.Config.set_library_file('C:/Program Files/LLVM/bin/libclang.dll')
            #cindex.Config.set_library_path('C:/Program Files/LLVM/bin')

        tu = cindex.Index.create().parse(self.path, args=self.flags)
        #self.out.indent = 0
        #self.out(self.header)
        self.out.indent = 1
        self.parse_overloads(tu.cursor)
        self.parse_definitions(tu.cursor)
        self.out.indent = 0
        #self.out(self.footer)
        #Jinja
        config = self.config
        print(self.config)
        config['body'] = self.out.string
        self.searchpath = Path('.')  / '__aimgen__'
        loader = jinja2.FileSystemLoader(searchpath=self.searchpath)
        env = jinja2.Environment(loader=loader)

        template = env.get_template(f'{self.name}.cpp')
        rendered = template.render(config)
        #print(rendered)
        filename = self.target
        with open(filename,'w') as fh:
            fh.write(rendered)

        #BASE_PATH = Path('.')
        #self.path = BASE_PATH / self.source
        #self.out = FileOut(open(BASE_PATH / self.target, 'w'))
