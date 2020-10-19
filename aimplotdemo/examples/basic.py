import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

import arcade

import aimgui
#from aimgui.impl.arcade import ArcadeGui
from aimgui.impl.arcade import ArcadeRenderer

import aimplot

class MyGui:
    def __init__(self, window, shared=False):
        self.shared = shared
        self.window = window
        aimgui.create_context()
        aimplot.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())

    def update(self, delta_time):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size( (512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Dockable Window#2')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()
        aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()

app = App()

arcade.run()
