import aimgui
from aimgui import rel

from aimdemo.page import Page


class ImageDraw(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def draw(self):
        aimgui.begin("Image example")
        draw_list = aimgui.get_window_draw_list()
        pos = rel(0,0)
        pos2 = self.texture.size[0] + pos[0], self.texture.size[1] + pos[1]
        draw_list.add_image(self.texture.glo.value, pos, pos2)
        aimgui.end()

def install(app):
    app.add_page(ImageDraw, "imagedraw", "Image Draw")
