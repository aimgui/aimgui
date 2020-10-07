from pathlib import Path

import arcade
import imgui
import imgui.core

from imdemo.page import Page

RESOURCE_PATH = Path(__file__).parent.parent / 'assets'

class FontPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        io = imgui.get_io()

        self.new_font = io.fonts.add_font_from_file_ttf(str(RESOURCE_PATH / "DroidSans.ttf"), 20)
        self.window.gui.renderer.refresh_font_texture()

    def draw(self):
        imgui.begin("Font")

        imgui.text("Text displayed using default font")
        with imgui.font(self.new_font):
            imgui.text("Text displayed using custom font")

        imgui.end()

def install(app):
    app.add_page(FontPage, "font", "Font")