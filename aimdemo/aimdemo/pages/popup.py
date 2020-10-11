import aimgui as gui

from aimdemo.page import Page


class Popup(Page):
    def draw(self):
        gui.begin("Example: simple popup")

        if gui.button("select"):
            gui.open_popup("select-popup")

        gui.same_line()

        if gui.begin_popup("select-popup"):
            gui.text("Select one")
            gui.separator()
            gui.selectable("One")
            gui.selectable("Two")
            gui.selectable("Three")
            gui.end_popup()

        gui.end()

class PopupContextView(Page):
    def draw(self):
        gui.begin("Example: popup context view")
        gui.text("Right-click to set value.")
        if gui.begin_popup_context_item("Item Context Menu", mouse_button=0):
            gui.selectable("Set to Zero")
            gui.end_popup()
        gui.end()

class PopupContextWindow(Page):
    def draw(self):
        gui.begin("Example: popup context window")
        if gui.begin_popup_context_window(mouse_button=0):
            gui.selectable("Clear")
            gui.end_popup()
        gui.end()

class PopupModal(Page):
    def draw(self):
        gui.begin("Example: simple popup modal")

        if gui.button("Open Modal popup"):
            gui.open_popup("select-popup")

        gui.same_line()

        if gui.begin_popup_modal("select-popup")[0]:
            gui.text("Select an option:")
            gui.separator()
            gui.selectable("One")
            gui.selectable("Two")
            gui.selectable("Three")
            gui.end_popup()

        gui.end()

def install(app):
    app.add_page(Popup, "popup", "Popup")
    app.add_page(PopupContextView, "popupcontextview", "Popup Context View")
    app.add_page(PopupContextWindow, "popupcontextwindow", "Popup Context Window")
    app.add_page(PopupModal, "popupmodal", "Popup Modal")

