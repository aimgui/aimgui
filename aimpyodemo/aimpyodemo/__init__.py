__version__ = '0.1.0'

import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

from pathlib import Path

import pyglet
import arcade
import aimgui

from .gui import PyoGui


class App(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, "AimPyo Demo", resizable=True)
        self.gui = PyoGui(self)
        self.sections = {}
        self.pages = {}
        self.page = None
        self.show_metrics = False
        self.show_style_editor = False
        self.resource_path = Path(__file__).parent.parent / 'resources'
        file_path = os.path.dirname(os.path.abspath(__file__))
        # print(file_path)
        os.chdir(file_path)


    def on_draw(self):
        super().on_draw()
        self.gui.render()

    def run(self):
        arcade.run()
        if self.page:
            self.page.close()

    def use(self, name):
        import importlib.util
        spec = importlib.util.find_spec(f"aimpyodemo.pages.{name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module, install = module, module.install
        install(self)

    def add_section(self, title):
        # print(page.__dict__)
        if not title in self.sections.keys():
            section = { 'title': title, 'pages':{}}
            self.sections[title] = section
        else:
            section = self.sections[title]
        return section

    def add_page(self, klass, section_title, title=None):
        # print(page.__dict__)
        name = klass.__name__.lower()
        if not title:
            title = klass.__name__
        section = self.add_section(section_title)
        entry = { 'klass': klass, 'name': name, 'title': title }
        self.pages[name] = entry
        section['pages'][name] = entry

    def show(self, name):
        def callback(delta_time):
            if self.page is not None:
                self.page.close()

            entry = self.pages[name]
            self.page = page = entry['klass'].create(self, name, entry['title'])
            self.show_view(page)
        pyglet.clock.schedule_once(callback, 0)