import aimgui

from aimdemo.page import Page


class Tooltip(Page):
    def draw(self):
        aimgui.begin("Example: tooltip")
        aimgui.button("Click me!")
        if aimgui.is_item_hovered():
            aimgui.begin_tooltip()
            aimgui.text("This button is clickable.")
            aimgui.text("This button has full window tooltip.")
            tex_id = aimgui.get_io().fonts.tex_id
            aimgui.image(tex_id, (512, 64), border_col=(1, 0, 0, 1))
            aimgui.end_tooltip()
        aimgui.end()

def install(app):
    app.add_page(Tooltip, "tooltip", "Tooltip")
