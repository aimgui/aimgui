import os
from pathlib import Path

import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer

RESOURCE_PATH = Path(__file__).parent.parent / 'resources'

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        self.texture = window.ctx.load_texture(RESOURCE_PATH / "robocute.png", flip=False)

    def draw(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        imgui.begin("Image example")
        draw_list = imgui.get_window_draw_list()
        #imgui.image(self.texture.glo, *self.texture.size)
        #draw_list.add_image(self.texture_id, (0, 0), (self.width, self.height))
        draw_list.add_image(self.texture.glo, (0, 0), self.texture.size)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Image Example", resizable=True)
        self.gui = MyGui(self)
        #
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
