import aimgui

from aimdemo.page import Page


class MousePage(Page):
    def draw(self):
        aimgui.begin(self.title)

        #aimgui.text(str(aimgui.is_mouse_down(0)))
        aimgui.label_text(str(aimgui.get_mouse_pos()), "position")
        aimgui.label_text(str(aimgui.is_mouse_down(0)), "left button")
        aimgui.label_text(str(aimgui.is_mouse_down(1)), "right button")
        aimgui.label_text(str(aimgui.is_mouse_down(2)), "middle button")

        aimgui.end()

def install(app):
    app.add_page(MousePage, "mouse", "Mouse")
