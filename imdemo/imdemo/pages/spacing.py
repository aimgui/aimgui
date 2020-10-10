import aimgui as gui

from imdemo.page import Page


class SpacingPage(Page):
    def draw(self):
        gui.begin(self.title)

        gui.text("Some text with bullets:")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet A")

        gui.spacing(); gui.spacing()

        gui.text("Another text with bullets:")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet A")

        gui.end()

def install(app):
    app.add_page(SpacingPage, "spacing", "Spacing")
