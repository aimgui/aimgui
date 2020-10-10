import aimgui as gui

from imdemo.page import Page


class SelectablePage(Page):
    def reset(self):
        self.selected = [False, False]

    def draw(self):
        gui.begin(self.title)
        _, self.selected[0] = gui.selectable(
            "1. I am selectable", self.selected[0]
        )
        _, self.selected[1] = gui.selectable(
            "2. I am selectable too", self.selected[1]
        )
        gui.text("3. I am not selectable")
        gui.end()

def install(app):
    app.add_page(SelectablePage, "selectable", "Selectable")
