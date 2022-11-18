__version__ = '0.1.0'

import os
from pathlib import Path

import pyglet
import arcade
import aimgui

from aimgui.impl.arcade import ArcadeGui

class App(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, "AimGui Demo", resizable=True)
        self.gui = ArcadeGui(self)
        self.pages = {}
        self.show_metrics = False
        self.show_style_editor = False
        self.resource_path = Path(__file__).parent.parent / 'resources'
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


    def on_draw(self):
        super().on_draw()
        self.gui.render()

    def run(self):
        arcade.run()

    def use(self, name):
        import importlib.util
        spec = importlib.util.find_spec(f"aimdemo.pages.{name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module, install = module, module.install
        install(self)

    def add_page(self, klass, name, title):
        self.pages[name] = { 'klass': klass, 'name': name, 'title': title }

    def show(self, name):
        def callback(delta_time):
            entry = self.pages[name]
            self.page = page = entry['klass'].create(self, name, entry['title'])
            self.show_view(page)
        pyglet.clock.schedule_once(callback, 0)