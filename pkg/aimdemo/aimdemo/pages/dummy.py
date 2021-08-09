import aimgui

from aimdemo.page import Page


class Dummy(Page):
    def draw(self):
        aimgui.begin("Example: dummy elements")

        aimgui.text("Some text with bullets:")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet B")

        aimgui.dummy((0, 50))
        aimgui.bullet_text("Text after dummy")

        aimgui.end()

def install(app):
    app.add_page(Dummy, "dummy", "Dummy")
