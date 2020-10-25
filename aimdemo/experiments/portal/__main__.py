import aimgui

from aimgui.impl.arcade import ArcadeGui

from experiments.portal.gui import ArcadePortalGui

import arcade

class InnerGui(ArcadePortalGui):
    def draw(self):
        aimgui.set_current_context(self.context)
        self.io.display_framebuffer_scale = (self.zoom, self.zoom)
        self.io.font_global_scale = self.zoom
        aimgui.new_frame()
        
        aimgui.set_next_window_size((500,500))
        aimgui.begin('Portal')
        aimgui.button("Button 3")
        aimgui.button("Button 4")

        pos_x, pos_y = self.io.mouse_pos
        sz = 10

        draw_list = aimgui.get_foreground_draw_list()
        draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(0))
        '''
        draw_list = aimgui.get_foreground_draw_list()
        pos_x = 10
        pos_y = 10
        sz = 20
        for i in range(0, aimgui.COL_COUNT):
            name = aimgui.get_style_color_name(i)
            pos_y = i*20
            draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(i))
            draw_list.add_text((pos_x+32, pos_y), aimgui.get_color_u32((1,1,1,1)), name)
        '''
        aimgui.end()

        aimgui.begin('Portal##2')
        aimgui.button("Button 3")
        aimgui.button("Button 4")
        aimgui.end()

        aimgui.end_frame()
        #print(self.position)
        super().draw()

class App(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, 'Portal Experiment', resizable=True)
        self.gui = ArcadeGui(self)
        self.inner_gui = InnerGui(self)

    def on_draw(self):
        arcade.start_render()

        aimgui.set_current_context(self.gui.context)
        aimgui.new_frame()

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        self.inner_gui.position = aimgui.get_cursor_screen_pos()
        self.inner_gui.size = (600, 400)
        aimgui.invisible_button("Blah", (600, 400))
        def cb(renderer, draw_data, draw_list, cmd, user_data):
            self.inner_gui.draw()
            aimgui.set_current_context(self.gui.context)
        draw_list = aimgui.get_window_draw_list()
        draw_list.add_callback(cb, None)
        #aimgui.set_current_context(self.gui.context)
        aimgui.end()

        #aimgui.show_metrics_window()
        aimgui.end_frame()

        self.gui.draw()
        #self.inner_gui.draw()


app = App()
arcade.run()
