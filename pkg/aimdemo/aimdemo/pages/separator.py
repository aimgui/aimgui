import aimgui

from aimdemo.page import Page


class SeparatorPage(Page):
    def draw(self):
        aimgui.begin(self.title)

        aimgui.text("Some text with bullets")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet A")

        aimgui.separator()

        aimgui.text("Another text with bullets")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet A")

        aimgui.end()

def install(app):
    app.add_page(SeparatorPage, "separator", "Separator")
