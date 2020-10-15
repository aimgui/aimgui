import aimgui

from aimdemo.page import Page


class WindowDraw(Page):
    
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        off = (0,0)
        def restore_offset_cb(renderer, draw_data, draw_list, cmd, user_data):
            renderer.offset = off


        aimgui.begin(self.title)

        clip = aimgui.get_cursor_screen_pos()

        def offset_cb(renderer, draw_data, draw_list, cmd, user_data):
            off = renderer.offset
            left = clip[0]
            bottom = -clip[1]
            renderer.offset = (left, -bottom)

        draw_list = aimgui.get_window_draw_list()
        draw_list.add_callback(offset_cb, None)

        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            pos_y = i*20
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(i))
            draw_list.add_text((pos_x+32, pos_y), aimgui.get_color_u32((1,1,1,1)), name)

        draw_list.add_callback(restore_offset_cb, None)

        aimgui.end()

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
