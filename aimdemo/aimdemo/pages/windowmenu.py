import aimgui as gui

from aimdemo.page import Page


class WindowMenu(Page):
    def draw(self):
        flags = gui.WINDOW_FLAGS_MENU_BAR

        gui.begin("Child Window - File Browser", flags=flags)

        if gui.begin_menu_bar():
            if gui.begin_menu('File'):
                gui.menu_item("Quit", 'Cmd+Q', False, True)
                gui.end_menu()

            gui.end_menu_bar()

        gui.end()

def install(app):
    app.add_page(WindowMenu, "windowmenu", "Window Menu")
