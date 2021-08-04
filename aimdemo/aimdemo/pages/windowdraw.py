import aimgui
from aimgui import rel

from aimdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        sz = 20
        draw_list = aimgui.get_window_draw_list()
        rgba_color = aimgui.get_color_u32((1, 1, 1, 1))
        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            color = aimgui.get_color_u32(aimgui.get_style_color_vec4(i))
            p1 = rel(0, i*10)
            p2 = (p1[0] + sz, p1[1] + sz)
            draw_list.add_rect_filled(p1, p2, color)
            
            p1 = rel(20, i*10)
            draw_list.add_text(p1, rgba_color, name)

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
