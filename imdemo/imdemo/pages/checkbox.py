import arcade
import aimgui as gui

from imdemo.page import Page


class Checkbox(Page):
    def reset(self):
        self.checkbox1_enabled = True
        self.checkbox2_enabled = False

    def draw(self):
        gui.begin("Example: checkboxes")

        # note: first element of return two-tuple notifies if there was a click
        #       event in currently processed frame and second element is actual
        #       checkbox state.
        _, self.checkbox1_enabled = gui.checkbox("Checkbox 1", self.checkbox1_enabled)
        _, self.checkbox2_enabled = gui.checkbox("Checkbox 2", self.checkbox2_enabled)

        gui.text("Checkbox 1 state value: {}".format(self.checkbox1_enabled))
        gui.text("Checkbox 2 state value: {}".format(self.checkbox2_enabled))

        gui.end()

class CheckboxFlags(Page):
    def reset(self):
        self.flags = gui.WINDOW_NO_RESIZE | gui.WINDOW_NO_MOVE

    def draw(self):
        gui.begin("Example: checkboxes for flags", flags=self.flags)

        clicked, self.flags = gui.checkbox_flags(
            "No resize", self.flags, gui.WINDOW_NO_RESIZE
        )
        clicked, self.flags = gui.checkbox_flags(
            "No move", self.flags, gui.WINDOW_NO_MOVE
        )
        clicked, self.flags = gui.checkbox_flags(
            "No collapse", self.flags, gui.WINDOW_NO_COLLAPSE
        )
        # note: it also allows to use multiple flags at once
        clicked, self.flags = gui.checkbox_flags(
            "No resize & no move", self.flags,
            gui.WINDOW_NO_RESIZE | gui.WINDOW_NO_MOVE
        )
        gui.text("Current flags value: {0:b}".format(self.flags))
        gui.end()

def install(app):
    app.add_page(Checkbox, "checkbox", "Checkbox")
    app.add_page(CheckboxFlags, "checkboxflags", "CheckboxFlags")


