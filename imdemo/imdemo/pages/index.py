import arcade
import aimgui as gui

from imdemo.page import Page


class Index(Page):
    def draw(self):
        gui.begin("Index")

        gui.text("Welcome to the Arcade ImGui Demo!")
        
        gui.end()

def install(app):
    app.add_page(Index, "index", "Index")