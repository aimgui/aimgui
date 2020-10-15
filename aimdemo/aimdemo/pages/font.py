from pathlib import Path

import aimgui

from aimdemo.page import Page

RESOURCE_PATH = Path(__file__).parent.parent / 'assets'

class FontPage(Page):
    def reset(self):
        io = aimgui.get_io()
        font_path = self.window.resource_path / 'DroidSans.ttf'
        self.font = io.fonts.add_font_from_file_ttf(str(font_path), 20)
        self.window.gui.renderer.refresh_font_texture()

    def draw(self):
        aimgui.begin("Font")

        aimgui.text("Text displayed using default font")
        '''
        with aimgui.font(self.font):
            aimgui.text("Text displayed using custom font")
        '''
        aimgui.push_font(self.font)
        aimgui.text("Text displayed using custom font")
        aimgui.pop_font()

        aimgui.end()

def install(app):
    app.add_page(FontPage, "font", "Font")