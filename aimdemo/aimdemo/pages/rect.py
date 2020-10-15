import aimgui

from aimdemo.page import Page


class Rect(Page):
    def draw(self):
        aimgui.begin("Rectangle")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_rect((20, 35), (90, 80), aimgui.get_color_u32((1,1,0,1)), thickness=3)
        draw_list.add_rect((110, 35), (180, 80), aimgui.get_color_u32((1,0,0,1)), rounding=5, thickness=3)
        aimgui.end()

class RectFilled(Page):
    def draw(self):
        aimgui.begin("Rectangle Filled")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_rect_filled((20, 35), (90, 80), aimgui.get_color_u32((1,1,0,1)))
        draw_list.add_rect_filled((110, 35), (180, 80), aimgui.get_color_u32((1,0,0,1)), 5)
        aimgui.end()

def install(app):
    app.add_page(Rect, "rect", "Rectangle")
    app.add_page(RectFilled, "rectfilled", "Rectangle Filled")
