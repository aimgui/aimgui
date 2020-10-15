import aimgui

from aimdemo.page import Page


class FontImage(Page):
    def draw(self):
        aimgui.begin("Image example")
        tex_id = aimgui.get_io().fonts.tex_id
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_image(tex_id, (128, 64), (512, 256), col=aimgui.get_color_u32((0.5,0.5,1,1)))
        aimgui.end()

def install(app):
    app.add_page(FontImage, "fontimage", "Font Image")
