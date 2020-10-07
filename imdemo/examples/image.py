import os
from pathlib import Path

import aimgui as gui
from aimgui.renderers.arcade import ArcadeRenderer
from aimgui import int_to_texid, texid_to_int

import arcade

RESOURCE_PATH = Path(__file__).parent.parent / 'resources'


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        gui.create_context()
        self.renderer = ArcadeRenderer(window)
        self.texture = window.ctx.load_texture(RESOURCE_PATH / "robocute.png", flip=False)

    def draw(self):
        gui.new_frame()

        gui.set_next_window_pos( (16, 32) )
        gui.set_next_window_size( (512, 512) )

        gui.begin("Image example")
        #gui.image(self.texture.glo, self.texture.size)
        gui.image(self.texture.glo.value, self.texture.size)
        gui.end()

        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Image Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
