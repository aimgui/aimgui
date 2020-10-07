import arcade
import aimgui as gui

from imdemo.page import Page


class Bullet(Page):
    def draw(self):
        gui.begin(self.title)

        for i in range(10):
            gui.bullet()

        gui.end()


class BulletText(Page):
    def draw(self):
        gui.begin(self.title)
        gui.bullet_text("Bullet 1")
        gui.bullet_text("Bullet 2")
        gui.bullet_text("Bullet 3")
        gui.end()

def install(app):
    app.add_page(Bullet, "bullet", "Bullets")
    app.add_page(BulletText,  "bullettext", "Bullets with Text")