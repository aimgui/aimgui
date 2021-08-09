import aimgui
from aimgui import rel
from aimgui.impl.arcade import ArcadeGui

from experiments.gig.gui import ArcadePortalGui

import arcade

class InnerGui(ArcadePortalGui):
    def draw(self):
        aimgui.set_current_context(self.context)
        #self.io.display_framebuffer_scale = (self.zoom, self.zoom)
        #self.io.font_global_scale = self.zoom
        aimgui.new_frame()
        
        aimgui.set_next_window_size((500,500))
        aimgui.begin('Portal')

        pos_x, pos_y = self.io.mouse_pos
        sz = 10

        draw_list = aimgui.get_foreground_draw_list()
        draw_list.add_rect_filled((pos_x, pos_y), (pos_x+sz, pos_y+sz), aimgui.get_color_u32(0))

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
        super().__init__(1280, 640, 'Gui in Gui Experiment', resizable=True)
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
        size = aimgui.get_content_region_max()
        self.inner_gui.size = size
        aimgui.invisible_button("Blah", size)
        self.inner_gui.hovered = aimgui.is_item_hovered()

        def cb(renderer, draw_data, draw_list, cmd, user_data):
            self.inner_gui.draw()
            aimgui.set_current_context(self.gui.context)

        draw_list = aimgui.get_window_draw_list()
        draw_list.add_callback(cb, None)

        aimgui.end()

        aimgui.show_metrics_window()
        aimgui.end_frame()

        self.gui.render()

app = App()
arcade.run()
