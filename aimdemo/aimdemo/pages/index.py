import arcade
import aimgui as gui

from aimdemo.page import Page


class Index(Page):
    def draw(self):
        gui.begin("Index")

        gui.text("Welcome to the AimGui Demo!")
        
        gui.end()

def install(app):
    app.add_page(Index, "index", "Index")