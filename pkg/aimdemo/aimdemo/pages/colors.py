import aimgui

from aimdemo.page import Page


class ColorsPage(Page):
    def draw(self):
        style = aimgui.get_style()
        
        aimgui.begin("Colors")
        aimgui.columns(4)
        for color in range(0, aimgui.COL_COUNT):
            aimgui.text(f"Color: {color}")
            aimgui.color_button(f"color#{color}", style.colors[color])
            aimgui.next_column()

        aimgui.end()

def install(app):
    app.add_page(ColorsPage, "colors", "Colors")
