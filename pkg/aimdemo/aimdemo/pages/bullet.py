import aimgui

from aimdemo.page import Page


class Bullet(Page):
    def draw(self):
        aimgui.begin(self.title)

        for i in range(10):
            aimgui.bullet()

        aimgui.end()


class BulletText(Page):
    def draw(self):
        aimgui.begin(self.title)
        aimgui.bullet_text("Bullet 1")
        aimgui.bullet_text("Bullet 2")
        aimgui.bullet_text("Bullet 3")
        aimgui.end()

def install(app):
    app.add_page(Bullet, "bullet", "Bullets")
    app.add_page(BulletText,  "bullettext", "Bullets with Text")