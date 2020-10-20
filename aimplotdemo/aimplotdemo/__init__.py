__version__ = '0.1.0'

import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

from pathlib import Path

import pyglet
import arcade
import aimgui

#from aimgui.impl.arcade import ArcadeGui
from aimgui.impl.arcade import ArcadeRenderer

import aimplot


class MyGui:
    def __init__(self, window):
        self.window = window
        aimgui.create_context()
        aimplot.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, "AimPlot Demo", resizable=True)
        self.gui = MyGui(self)
        self.pages = {}
        self.show_metrics = False
        self.show_style_editor = False
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
        spec = importlib.util.find_spec(f"aimplotdemo.pages.{name}")
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