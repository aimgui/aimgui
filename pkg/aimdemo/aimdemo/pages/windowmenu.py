import aimgui

from aimdemo.page import Page


class WindowMenu(Page):
    def draw(self):
        flags = aimgui.WINDOW_FLAGS_MENU_BAR

        aimgui.begin("Child Window - File Browser", flags=flags)

        if aimgui.begin_menu_bar():
            if aimgui.begin_menu('File'):
                aimgui.menu_item("Quit", 'Cmd+Q', False, True)
                aimgui.end_menu()

            aimgui.end_menu_bar()

        aimgui.end()

def install(app):
    app.add_page(WindowMenu, "windowmenu", "Window Menu")
