import arcade
import aimgui

from . import Page


class Index(Page):
    def draw(self):
        aimgui.begin("Index")

        aimgui.text("Welcome to the AimPyo Demo!")
        
        aimgui.end()

def install(app):
    app.add_page(Index, "index", "Index")