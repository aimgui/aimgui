import aimgui as gui

from aimdemo.page import Page


class FontImage(Page):
    def draw(self):
        gui.begin("Image example")
        tex_id = gui.get_io().fonts.tex_id
        draw_list = gui.get_window_draw_list()
        draw_list.add_image(tex_id, (20, 35), (180, 80), col=gui.get_color_u32((0.5,0.5,1,1)))
        gui.end()

def install(app):
    app.add_page(FontImage, "fontimage", "Font Image")
