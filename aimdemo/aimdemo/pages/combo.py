import aimgui as gui

from aimdemo.page import Page


class Combo(Page):
    def reset(self):
        self.options = ["first", "second", "third"]
        self.current = 2

    def draw(self):
        gui.begin("Example: combo widget")

        clicked, self.current = gui.combo(
            "combo", self.current, self.options
        )
        gui.text(f"You chose:  {self.options[self.current]}")
        gui.end()

def install(app):
    app.add_page(Combo, "combo", "Combo")
