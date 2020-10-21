import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

import numpy as np

import arcade

import aimgui
from aimgui.impl.arcade import ArcadeGui

import aimplot

class MyGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window)
        aimplot.create_context()


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = MyGui(self)
        self.a = np.random.rand(10)
        self.b = np.random.rand(10)

    def on_draw(self):
        arcade.start_render()
        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Line Plot')

        if aimplot.begin_plot("My Plot"):
            aimplot.plot_line("A", self.a, 10)
            aimplot.plot_line("B", self.b, 10)
            #aimplot.plot_bars("B", self.values, 10)
            aimplot.end_plot()

        aimgui.end()
        #aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()

app = App()

arcade.run()
