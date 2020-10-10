import aimgui as gui

from imdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        draw_list = gui.get_window_draw_list()

        for i in range(0, gui.COLOR_COUNT):
            name = gui.get_style_color_name(i)
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), gui.get_color_u32(i))
            gui.dummy((sz, sz))
            gui.same_line()

        rgba_color = gui.get_color_u32((1, 1, 0, 1))
        draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), rgba_color)

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
