import aimgui as gui

from aimdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        gui.begin(self.title)
        draw_list = gui.get_window_draw_list()
        for i in range(0, gui.COLOR_COUNT):
            name = gui.get_style_color_name(i)
            pos_y = i*10
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), gui.get_color_u32(i))
        gui.end()

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
