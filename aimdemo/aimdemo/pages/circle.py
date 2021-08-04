import aimgui
from aimgui import rel

from aimdemo.page import Page


class Circle(Page):
    def draw(self):
        aimgui.begin("Circle")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_circle(rel(100, 60), 30, aimgui.get_color_u32((1,1,0,1)), thickness=3)
        aimgui.end()

class CircleFilled(Page):
    def draw(self):
        aimgui.begin("Filled")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_circle_filled(rel(100, 60), 30, aimgui.get_color_u32((1,1,0,1)))
        aimgui.end()

def install(app):
    app.add_page(Circle, "circle", "Circle")
    app.add_page(CircleFilled, "circlefilled", "Filled Circle")


