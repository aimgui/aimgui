import aimgui

from aimdemo.page import Page


class DemoPage(Page):
    def draw(self):
        aimgui.show_demo_window()

def install(app):
    app.add_page(DemoPage, 'demo', 'Demo in Demo')
