import aimgui

from aimdemo.page import Page


class PortalPage(Page):
    
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        aimgui.begin(self.title)

        portal = aimgui.get_cursor_screen_pos()
        draw_list = aimgui.get_window_draw_list()
        self.window.gui.push_portal(draw_list, portal)

        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            pos_y = i*20
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(i))
            draw_list.add_text((pos_x+32, pos_y), aimgui.get_color_u32((1,1,1,1)), name)

        self.window.gui.pop_portal(draw_list)

        aimgui.end()

def install(app):
    app.add_page(PortalPage, "portal", "Portal")
