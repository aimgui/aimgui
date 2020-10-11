import aimgui as gui

from aimdemo.page import Page


class FontImage(Page):
    def draw(self):
        gui.begin("Image example")
        texture_id = gui.get_io().fonts.texture_id
        draw_list = gui.get_window_draw_list()
        draw_list.add_image(texture_id, (20, 35), (180, 80), col=gui.get_color_u32_rgba(0.5,0.5,1,1))
        gui.end()

def install(app):
    app.add_page(FontImage, "fontimage", "Font Image")
