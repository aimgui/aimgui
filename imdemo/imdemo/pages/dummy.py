import aimgui as gui

from imdemo.page import Page


class Dummy(Page):
    def draw(self):
        gui.begin("Example: dummy elements")

        gui.text("Some text with bullets:")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet B")

        gui.dummy((0, 50))
        gui.bullet_text("Text after dummy")

        gui.end()

def install(app):
    app.add_page(Dummy, "dummy", "Dummy")
