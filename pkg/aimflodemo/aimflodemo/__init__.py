import os

import pyglet
import arcade

import aimgui
from aimgui.impl.arcade import ArcadeGui

import aimnodes

class App(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, "AimFlo Demo", resizable=True)
        self.gui = ArcadeGui(self)
        self.pages = {}
        self.show_metrics = False
        print(dir(aimnodes))
        print(aimnodes.create_context)
        print(aimnodes.push_attribute_flag)
        aimnodes.create_context()
        aimnodes.push_attribute_flag(aimnodes.ATTRIBUTE_FLAGS_ENABLE_LINK_DETACH_WITH_DRAG_CLICK)
        io = aimnodes.get_io()
        #TODO:Looks too scary to wrap.
        #io.link_detach_with_modifier_click.modifier = aimgui.get_io().key_ctrl

    def on_draw(self):
        super().on_draw()
        self.gui.render()

    def run(self):
        arcade.run()

    def use(self, name):
        import importlib.util
        spec = importlib.util.find_spec(f"aimflodemo.pages.{name}")
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