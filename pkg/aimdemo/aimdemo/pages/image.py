import aimgui

from aimdemo.page import Page


class ImagePage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def draw(self):
        aimgui.begin(self.title)
        aimgui.image(self.texture.glo.value, self.texture.size)
        aimgui.end()

def install(app):
    app.add_page(ImagePage, "image", "Image")
