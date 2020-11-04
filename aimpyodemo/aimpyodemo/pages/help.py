import arcade
import aimgui

from . import Page


class AboutPage(Page):
    def draw(self):
        aimgui.begin("Index")

        aimgui.text("Welcome to the AimPyo Demo!")
        
        aimgui.end()

def install(app):
    app.add_page(AboutPage, "help", "about", "About")