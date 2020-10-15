import aimgui

from aimdemo.page import Page


class Line(Page):
    def draw(self):
        aimgui.begin("Line")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_line((20, 35), (180, 80), aimgui.get_color_u32((1,1,0,1)), 3)
        draw_list.add_line((180, 35), (20, 80), aimgui.get_color_u32((1,0,0,1)), 3)
        aimgui.end()

class PolyLine(Page):
    def draw(self):
        aimgui.begin("Poly Line")
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], aimgui.get_color_u32((1,1,0,1)), closed=False, thickness=3)
        draw_list.add_polyline([(110, 35), (180, 35), (145, 80)],  aimgui.get_color_u32((1,0,0,1)), closed=True, thickness=3)
        aimgui.end()

def install(app):
    app.add_page(Line, "line", "Line")
    app.add_page(PolyLine, "polyline", "Poly Line")
