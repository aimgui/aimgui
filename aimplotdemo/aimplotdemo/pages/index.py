import arcade
import aimgui

from aimplotdemo.page import Page


class Index(Page):
    def draw(self):
        aimgui.begin("Index")

        aimgui.text("Welcome to the AimPlot Demo!")
        
        aimgui.end()

def install(app):
    app.add_page(Index, "index", "Index")