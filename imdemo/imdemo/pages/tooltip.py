import aimgui as gui

from imdemo.page import Page


class Tooltip(Page):
    def draw(self):
        gui.begin("Example: tooltip")
        gui.button("Click me!")
        if gui.is_item_hovered():
            gui.begin_tooltip()
            gui.text("This button is clickable.")
            gui.text("This button has full window tooltip.")
            tex_id = gui.get_io().fonts.tex_id
            gui.image(tex_id, (512, 64), border_col=(1, 0, 0, 1))
            gui.end_tooltip()
        gui.end()

def install(app):
    app.add_page(Tooltip, "tooltip", "Tooltip")
