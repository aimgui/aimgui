import aimgui as gui

from imdemo.page import Page


class SameLinePage(Page):
    def draw(self):
        gui.begin("Example: same line widgets")

        gui.text("same_line() with defaults:")
        gui.button("yes"); gui.same_line()
        gui.button("no")

        gui.text("same_line() with fixed position:")
        gui.button("yes"); gui.same_line(50)
        gui.button("no")

        gui.text("same_line() with spacing:")
        gui.button("yes"); gui.same_line(50)
        gui.button("no")

        gui.end()

def install(app):
    app.add_page(SameLinePage, "sameline", "Same Line")
