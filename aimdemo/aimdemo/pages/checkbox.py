import aimgui

from aimdemo.page import Page


class Checkbox(Page):
    def reset(self):
        self.checkbox1_enabled = True
        self.checkbox2_enabled = False

    def draw(self):
        aimgui.begin("Example: checkboxes")

        # note: first element of return two-tuple notifies if there was a click
        #       event in currently processed frame and second element is actual
        #       checkbox state.
        _, self.checkbox1_enabled = aimgui.checkbox("Checkbox 1", self.checkbox1_enabled)
        _, self.checkbox2_enabled = aimgui.checkbox("Checkbox 2", self.checkbox2_enabled)

        aimgui.text("Checkbox 1 state value: {}".format(self.checkbox1_enabled))
        aimgui.text("Checkbox 2 state value: {}".format(self.checkbox2_enabled))

        aimgui.end()

class CheckboxFlags(Page):
    def reset(self):
        self.flags = aimgui.WINDOW_FLAGS_NO_RESIZE | aimgui.WINDOW_FLAGS_NO_MOVE

    def draw(self):
        aimgui.begin("Example: checkboxes for flags", flags=self.flags)

        clicked, self.flags = aimgui.checkbox_flags(
            "No resize", self.flags, aimgui.WINDOW_FLAGS_NO_RESIZE
        )
        clicked, self.flags = aimgui.checkbox_flags(
            "No move", self.flags, aimgui.WINDOW_FLAGS_NO_MOVE
        )
        clicked, self.flags = aimgui.checkbox_flags(
            "No collapse", self.flags, aimgui.WINDOW_FLAGS_NO_COLLAPSE
        )
        # note: it also allows to use multiple flags at once
        clicked, self.flags = aimgui.checkbox_flags(
            "No resize & no move", self.flags,
            aimgui.WINDOW_FLAGS_NO_RESIZE | aimgui.WINDOW_FLAGS_NO_MOVE
        )
        aimgui.text("Current flags value: {0:b}".format(self.flags))
        aimgui.end()

def install(app):
    app.add_page(Checkbox, "checkbox", "Checkbox")
    app.add_page(CheckboxFlags, "checkboxflags", "CheckboxFlags")


