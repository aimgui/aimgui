import os

import pyglet
import arcade

import aimgui

from aimgui.impl.arcade import ArcadeGui

class App(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "AimFlo Demo", resizable=True)
        self.gui = ArcadeGui(self)
        self.pages = {}
        self.show_metrics = False

    def on_draw(self):
        super().on_draw()
        self.gui.draw()

    def run(self):
        arcade.run()

    def use(self, name):
        import importlib.util
        spec = importlib.util.find_spec(f"aimflo.pages.{name}")
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