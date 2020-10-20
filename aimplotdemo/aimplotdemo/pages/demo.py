import aimgui
import aimplot

from aimplotdemo.page import Page


class DemoPage(Page):
    def draw(self):
        aimplot.show_demo_window()

def install(app):
    app.add_page(DemoPage, 'demo', 'Demo in Demo')
