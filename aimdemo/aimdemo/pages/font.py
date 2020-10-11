from pathlib import Path

import aimgui as gui

from aimdemo.page import Page

RESOURCE_PATH = Path(__file__).parent.parent / 'assets'

class FontPage(Page):
    def reset(self):
        io = gui.get_io()

        self.font = io.fonts.add_font_from_file_ttf(str(RESOURCE_PATH / "DroidSans.ttf"), 20)
        self.window.gui.renderer.refresh_font_texture()

    def draw(self):
        gui.begin("Font")

        gui.text("Text displayed using default font")
        '''
        with gui.font(self.font):
            gui.text("Text displayed using custom font")
        '''
        gui.push_font(self.font)
        gui.text("Text displayed using custom font")
        gui.pop_font()

        gui.end()

def install(app):
    app.add_page(FontPage, "font", "Font")