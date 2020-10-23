import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

import numpy as np

import arcade

import aimgui
from aimgui.impl.arcade import ArcadeGui

import aimnodes

class MyGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window)
        aimnodes.initialize()


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

        aimgui.begin('Nodes')

        aimnodes.begin_node_editor()
        aimnodes.begin_node(1)
        aimnodes.begin_node_title_bar()
        aimgui.text('Test')
        aimnodes.end_node_title_bar()

        aimnodes.end_node()
        aimnodes.end_node_editor()

        aimgui.end()
        #aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()

app = App()

arcade.run()
