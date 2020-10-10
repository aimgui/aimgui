import aimgui as gui

from imdemo.page import Page


class Rect(Page):
    def draw(self):
        gui.begin("Rectangle")
        draw_list = gui.get_window_draw_list()
        draw_list.add_rect((20, 35), (90, 80), gui.get_color_u32((1,1,0,1)), thickness=3)
        draw_list.add_rect((110, 35), (180, 80), gui.get_color_u32((1,0,0,1)), rounding=5, thickness=3)
        gui.end()

class RectFilled(Page):
    def draw(self):
        gui.begin("Rectangle Filled")
        draw_list = gui.get_window_draw_list()
        draw_list.add_rect_filled((20, 35), (90, 80), gui.get_color_u32((1,1,0,1)))
        draw_list.add_rect_filled((110, 35), (180, 80), gui.get_color_u32((1,0,0,1)), 5)
        gui.end()

def install(app):
    app.add_page(Rect, "rect", "Rectangle")
    app.add_page(RectFilled, "rectfilled", "Rectangle Filled")
