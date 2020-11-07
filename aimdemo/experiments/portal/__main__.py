import aimgui
from experiments.portal.gui import ArcadeGui

import arcade

class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, 'Portal Experiment', resizable=True)
        self.gui = ArcadeGui(self)

    def on_draw(self):
        arcade.start_render()

        aimgui.new_frame()

        pos_x = 10
        pos_y = 10
        sz = 20
        
        aimgui.begin('Portal')

        portal = aimgui.get_cursor_screen_pos()
        draw_list = aimgui.get_window_draw_list()
        self.gui.push_portal(draw_list, portal)
        region = aimgui.get_content_region_max()
        print(region)
        aimgui.push_clip_rect((0,0), region, False)
        #draw_list.push_clip_rect_full_screen()
        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            pos_y = i*20
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(i))
            draw_list.add_text((pos_x+32, pos_y), aimgui.get_color_u32((1,1,1,1)), name)

        aimgui.pop_clip_rect()

        self.gui.pop_portal(draw_list)

        aimgui.end()

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        aimgui.end()

        aimgui.end_frame()

        self.gui.render()


app = App()
arcade.run()
