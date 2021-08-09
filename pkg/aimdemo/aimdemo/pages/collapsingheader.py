import aimgui

from aimdemo.page import Page


class CollapsingHeader(Page):
    def reset(self):
        self.visible = True

    def draw(self):
        aimgui.begin("Example: collapsing header")
        expanded, self.visible = aimgui.collapsing_header("Expand me!", self.visible)

        if expanded:
            aimgui.text("Now you see me!")
        aimgui.end()

def install(app):
    app.add_page(CollapsingHeader, "collapsingheader", "Collapsing Header")
