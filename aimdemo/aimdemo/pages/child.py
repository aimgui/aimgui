import aimgui

from aimdemo.page import Page


class Child(Page):
    def draw(self):
        aimgui.begin("Example: child region")

        #aimgui.begin_child("region", (150, -50), border=True)
        aimgui.begin_child("region", border=True)
        aimgui.text("inside region")
        aimgui.end_child()

        aimgui.text("outside region")
        aimgui.end()

def install(app):
    app.add_page(Child, "child", "Child")
