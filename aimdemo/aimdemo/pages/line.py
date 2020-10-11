import aimgui as gui

from aimdemo.page import Page


class Line(Page):
    def draw(self):
        gui.begin("Line")
        draw_list = gui.get_window_draw_list()
        draw_list.add_line((20, 35), (180, 80), gui.get_color_u32((1,1,0,1)), 3)
        draw_list.add_line((180, 35), (20, 80), gui.get_color_u32((1,0,0,1)), 3)
        gui.end()

class PolyLine(Page):
    def draw(self):
        gui.begin("Poly Line")
        draw_list = gui.get_window_draw_list()
        draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], 3, gui.get_color_u32((1,1,0,1)), closed=False, thickness=3)
        draw_list.add_polyline([(110, 35), (180, 35), (145, 80)], 3, gui.get_color_u32((1,0,0,1)), closed=True, thickness=3)
        gui.end()

def install(app):
    app.add_page(Line, "line", "Line")
    app.add_page(PolyLine, "polyline", "Poly Line")
