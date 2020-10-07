import os

import arcade
import imgui
import imgui.core

from imdemo.page import Page


class ImageDraw(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def draw(self):
        imgui.begin("Image example")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_image(self.texture.glo, (0, 0), self.texture.size)
        imgui.end()

def install(app):
    app.add_page(ImageDraw, "imagedraw", "Image Draw")
