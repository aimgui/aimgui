import aimgui

from aimdemo.page import Page


class Combo(Page):
    def reset(self):
        self.options = ["first", "second", "third"]
        self.current = 2

    def draw(self):
        aimgui.begin("Example: combo widget")

        clicked, self.current = aimgui.combo(
            "combo", self.current, self.options
        )
        aimgui.text(f"You chose:  {self.options[self.current]}")
        aimgui.end()

def install(app):
    app.add_page(Combo, "combo", "Combo")
