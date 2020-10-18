import aimgui

from aimdemo.page import Page


class Popup(Page):
    def draw(self):
        aimgui.begin("Example: simple popup")

        if aimgui.button("select"):
            aimgui.open_popup("select-popup")

        aimgui.same_line()

        if aimgui.begin_popup("select-popup"):
            aimgui.text("Select one")
            aimgui.separator()
            aimgui.selectable("One", False)
            aimgui.selectable("Two", False)
            aimgui.selectable("Three", False)
            aimgui.end_popup()

        aimgui.end()

class PopupContextView(Page):
    def draw(self):
        aimgui.begin("Example: popup context view")
        aimgui.text("Right-click to set value.")
        if aimgui.begin_popup_context_item("Item Context Menu"):
            aimgui.selectable("Set to Zero", True)
            aimgui.end_popup()
        aimgui.end()

class PopupContextWindow(Page):
    def draw(self):
        aimgui.begin("Example: popup context window")
        if aimgui.begin_popup_context_window():
            aimgui.selectable("Clear", True)
            aimgui.end_popup()
        aimgui.end()

class PopupModal(Page):
    def draw(self):
        aimgui.begin("Example: simple popup modal")

        if aimgui.button("Open Modal popup"):
            aimgui.open_popup("select-popup")

        aimgui.same_line()

        if aimgui.begin_popup_modal("select-popup")[0]:
            aimgui.text("Select an option:")
            aimgui.separator()
            aimgui.selectable("One", False)
            aimgui.selectable("Two", False)
            aimgui.selectable("Three", False)
            aimgui.end_popup()

        aimgui.end()

def install(app):
    app.add_page(Popup, "popup", "Popup")
    app.add_page(PopupContextView, "popupcontextview", "Popup Context View")
    app.add_page(PopupContextWindow, "popupcontextwindow", "Popup Context Window")
    app.add_page(PopupModal, "popupmodal", "Popup Modal")

