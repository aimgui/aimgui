import aimgui as gui

from imdemo.page import Page


class Child(Page):
    def draw(self):
        gui.begin("Example: child region")

        gui.begin_child("region", (150, -50), border=True)
        gui.text("inside region")
        gui.end_child()

        gui.text("outside region")
        gui.end()

def install(app):
    app.add_page(Child, "child", "Child")
