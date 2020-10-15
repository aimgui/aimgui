import aimgui as gui

from aimdemo.page import Page


class ColorsPage(Page):
    def draw(self):
        style = gui.get_style()
        
        gui.begin("Colors")
        gui.columns(4)
        for color in range(0, gui.COL_COUNT):
            gui.text(f"Color: {color}")
            gui.color_button(f"color#{color}", style.colors[color])
            gui.next_column()

        gui.end()

def install(app):
    app.add_page(ColorsPage, "colors", "Colors")
