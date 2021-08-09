import aimgui
from aimgui import rel

from aimdemo.page import Page


class Line(Page):
    def draw(self):
        aimgui.begin("Line")
        draw_list = aimgui.get_window_draw_list()
        p1 = rel(20, 35)
        p2 = rel(180, 80)
        draw_list.add_line(p1, p2, aimgui.get_color_u32((1,1,0,1)), 3)
        p1 = rel(180, 35)
        p2 = rel(20, 80)
        draw_list.add_line(p1, p2, aimgui.get_color_u32((1,0,0,1)), 3)
        aimgui.end()

class PolyLine(Page):
    def draw(self):
        aimgui.begin("Poly Line")
        draw_list = aimgui.get_window_draw_list()
        p1 = rel(20, 35)
        p2 = rel(90, 35)
        p3 = rel(55, 80)
        draw_list.add_polyline([p1, p2, p3], aimgui.get_color_u32((1,1,0,1)), closed=False, thickness=3)
        p1 = rel(110, 35)
        p2 = rel(180, 35)
        p3 = rel(145, 80)
        draw_list.add_polyline([p1, p2, p3],  aimgui.get_color_u32((1,0,0,1)), closed=True, thickness=3)
        aimgui.end()

def install(app):
    app.add_page(Line, "line", "Line")
    app.add_page(PolyLine, "polyline", "Poly Line")
