import sys, os
sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)

import numpy as np

import arcade

import aimgui
from aimgui.impl.arcade import ArcadeGui

import aimbp

unique_id = 1

def gen_id():
    global unique_id
    result = unique_id
    unique_id += 1
    return result

class MyGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window)
        self.bp_context = aimbp.create_editor()


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = MyGui(self)
        self.links = []
        self.link_id = 0

    def add_link(self, id1, id2):
        self.links.append((self.link_id, id1, id2))
        self.link_id += 1
        return self.links[-1]

    def on_draw(self):

        arcade.start_render()
        aimgui.new_frame()

        aimbp.set_current_editor(self.gui.bp_context)

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Nodes')

        aimbp.begin('Nodes')

        #Start drawing nodes.
        aimbp.begin_node(1)
        aimgui.text("Node A")
        aimbp.begin_pin(2, aimbp.PinKind.INPUT)
        aimgui.text("-> In")
        aimbp.end_pin()
        aimgui.same_line()
        aimbp.begin_pin(3, aimbp.PinKind.OUTPUT)
        aimgui.text("Out ->")
        aimbp.end_pin()
        aimbp.end_node()

        aimbp.begin_node(4)
        aimgui.text("Node B")
        aimbp.begin_pin(5, aimbp.PinKind.INPUT)
        aimgui.text("-> In")
        aimbp.end_pin()
        aimgui.same_line()
        aimbp.begin_pin(6, aimbp.PinKind.OUTPUT)
        aimgui.text("Out ->")
        aimbp.end_pin()
        aimbp.end_node()
        
        if aimbp.begin_create():
            print('begin create')
            if (result := aimbp.query_new_link())[0]:
                print(result[1], result[2])
                if aimbp.accept_new_item():
                    print('accepted')
                    link = self.add_link(result[1], result[2])
                    aimbp.link(link[0], link[1], link[2])
        aimbp.end_create()

        for link in self.links:
            aimbp.link(link[0], link[1], link[2])

        aimbp.end()

        aimgui.end()
        #aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()

app = App()

arcade.run()
