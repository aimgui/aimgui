import aimgui

from aimdemo.page import Page


class SpacingPage(Page):
    def draw(self):
        aimgui.begin(self.title)

        aimgui.text("Some text with bullets:")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet A")

        aimgui.spacing(); aimgui.spacing()

        aimgui.text("Another text with bullets:")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet A")

        aimgui.end()

def install(app):
    app.add_page(SpacingPage, "spacing", "Spacing")
