__version__ = '0.1.0'

import os
from pathlib import Path

import pyglet
import arcade
import aimgui

from aimgui.renderers.arcade import ArcadeRenderer

class Gui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        aimgui.create_context()

        self.renderer = ArcadeRenderer(window)

    def draw(self):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())

class App(arcade.Window):
    def __init__(self):
        #super().__init__(1024, 768, "AimGui Demo", resizable=True)
        super().__init__(1280, 640, "AimGui Demo", resizable=True)
        self.gui = Gui(self)
        self.pages = {}
        self.view_metrics = False
        self.resource_path = Path(__file__).parent.parent / 'resources'
        file_path = os.path.dirname(os.path.abspath(__file__))
        # print(file_path)
        os.chdir(file_path)


    def on_draw(self):
        super().on_draw()
        self.gui.draw()

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
        # print(page.__dict__)
        self.pages[name] = { 'klass': klass, 'name': name, 'title': title }

    def show(self, name):
        def callback(delta_time):
            entry = self.pages[name]
            self.page = page = entry['klass'].create(self, name, entry['title'])
            self.show_view(page)
        pyglet.clock.schedule_once(callback, 0)