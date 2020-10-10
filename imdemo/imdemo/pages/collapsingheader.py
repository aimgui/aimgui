import aimgui as gui

from imdemo.page import Page


class CollapsingHeader(Page):
    def reset(self):
        self.visible = True

    def draw(self):
        gui.begin("Example: collapsing header")
        expanded, self.visible = gui.collapsing_header("Expand me!", self.visible)

        if expanded:
            gui.text("Now you see me!")
        gui.end()

def install(app):
    app.add_page(CollapsingHeader, "collapsingheader", "Collapsing Header")
