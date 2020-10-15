import aimgui

from aimdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        aimgui.begin(self.title)
        draw_list = aimgui.get_window_draw_list()
        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            pos_y = i*10
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(i))
        aimgui.end()

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
