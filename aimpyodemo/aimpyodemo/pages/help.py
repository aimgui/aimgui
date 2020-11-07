import arcade
import aimgui

from . import Page


class About(Page):
    def draw(self):
        aimgui.begin(self.title)

        aimgui.text("Welcome to the AimPyo Demo!")
        
        aimgui.end()

def install(app):
    app.add_page(About, "help")