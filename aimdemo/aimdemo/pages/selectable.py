import aimgui

from aimdemo.page import Page


class SelectablePage(Page):
    def reset(self):
        self.selected = [False, False]

    def draw(self):
        aimgui.begin(self.title)
        _, self.selected[0] = aimgui.selectable(
            "1. I am selectable", self.selected[0]
        )
        _, self.selected[1] = aimgui.selectable(
            "2. I am selectable too", self.selected[1]
        )
        aimgui.text("3. I am not selectable")
        aimgui.end()

def install(app):
    app.add_page(SelectablePage, "selectable", "Selectable")
