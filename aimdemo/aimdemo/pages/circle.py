import aimgui as gui

from aimdemo.page import Page


class Circle(Page):
    def draw(self):
        gui.begin("Circle")
        draw_list = gui.get_window_draw_list()
        draw_list.add_circle((100, 60), 30, gui.get_color_u32((1,1,0,1)), thickness=3)
        gui.end()

class CircleFilled(Page):
    def draw(self):
        gui.begin("Filled")
        draw_list = gui.get_window_draw_list()
        draw_list.add_circle_filled((100, 60), 30, gui.get_color_u32((1,1,0,1)))
        gui.end()

def install(app):
    app.add_page(Circle, "circle", "Circle")
    app.add_page(CircleFilled, "circlefilled", "Filled Circle")


