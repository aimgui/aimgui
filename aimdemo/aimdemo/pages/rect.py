import aimgui
from aimgui import rel

from aimdemo.page import Page


class Rect(Page):
    def draw(self):
        aimgui.begin("Rectangle")
        draw_list = aimgui.get_window_draw_list()
        p1 = rel(20, 35)
        p2 = rel(90, 80)
        draw_list.add_rect(p1, p2, aimgui.get_color_u32((1,1,0,1)), thickness=3)
        p1 = rel(110, 35)
        p2 = rel(180, 80)
        draw_list.add_rect(p1, p2, aimgui.get_color_u32((1,0,0,1)), rounding=5, thickness=3)
        aimgui.end()

class RectFilled(Page):
    def draw(self):
        aimgui.begin("Rectangle Filled")
        draw_list = aimgui.get_window_draw_list()
        p1 = rel(20, 35)
        p2 = rel(90, 80)
        draw_list.add_rect_filled(p1, p2, aimgui.get_color_u32((1,1,0,1)))
        p1 = rel(110, 35)
        p2 = rel(180, 80)
        draw_list.add_rect_filled(p1, p2, aimgui.get_color_u32((1,0,0,1)), 5)
        aimgui.end()

def install(app):
    app.add_page(Rect, "rect", "Rectangle")
    app.add_page(RectFilled, "rectfilled", "Rectangle Filled")
