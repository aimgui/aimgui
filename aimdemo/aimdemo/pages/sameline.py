import aimgui

from aimdemo.page import Page


class SameLinePage(Page):
    def draw(self):
        aimgui.begin("Example: same line widgets")

        aimgui.text("same_line() with defaults:")
        aimgui.button("yes"); aimgui.same_line()
        aimgui.button("no")

        aimgui.text("same_line() with fixed position:")
        aimgui.button("yes"); aimgui.same_line(100)
        aimgui.button("no")

        aimgui.text("same_line() with spacing:")
        aimgui.button("yes"); aimgui.same_line(0, 50)
        aimgui.button("no")

        aimgui.end()

def install(app):
    app.add_page(SameLinePage, "sameline", "Same Line")
