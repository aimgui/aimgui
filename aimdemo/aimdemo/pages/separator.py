import aimgui as gui

from aimdemo.page import Page


class SeparatorPage(Page):
    def draw(self):
        gui.begin(self.title)

        gui.text("Some text with bullets")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet A")

        gui.separator()

        gui.text("Another text with bullets")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet A")

        gui.end()

def install(app):
    app.add_page(SeparatorPage, "separator", "Separator")
