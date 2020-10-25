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

    def on_draw(self):

        arcade.start_render()
        aimgui.new_frame()

        aimbp.set_current_editor(self.gui.bp_context)

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Nodes')

        aimbp.begin('Nodes')

        #Start drawing nodes.
        aimbp.begin_node(gen_id())
        aimgui.text("Node A")
        aimbp.begin_pin(gen_id(), aimbp.PinKind.INPUT)
        aimgui.text("-> In")
        aimbp.end_pin()
        aimgui.same_line()
        aimbp.begin_pin(gen_id(), aimbp.PinKind.OUTPUT)
        aimgui.text("Out ->")
        aimbp.end_pin()
        aimbp.end_node()

        '''
        aimbp.begin_node(gen_id())
        aimgui.text("Node B")
        aimbp.begin_pin(gen_id(), aimbp.PinKind.INPUT)
        aimgui.text("-> In")
        aimbp.end_pin()
        aimgui.same_line()
        aimbp.begin_pin(gen_id(), aimbp.PinKind.OUTPUT)
        aimgui.text("Out ->")
        aimbp.end_pin()
        aimbp.end_node()
        '''
        
        aimbp.end()

        aimgui.end()
        aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()
    '''
    def on_draw(self):
        arcade.start_render()
        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Nodes')

        aimnodes.begin_node_editor()

        # Node 1
        aimnodes.begin_node(1)
        
        aimnodes.begin_node_title_bar()
        aimgui.text('Output')
        aimnodes.end_node_title_bar()

        aimnodes.begin_output_attribute(1)
        aimgui.text('output')
        aimnodes.end_output_attribute()

        aimnodes.end_node()

        # Node 2
        aimnodes.begin_node(2)
        
        aimnodes.begin_node_title_bar()
        aimgui.text('Input')
        aimnodes.end_node_title_bar()

        aimnodes.begin_input_attribute(2)
        aimgui.text('input')
        aimnodes.end_input_attribute()

        aimnodes.end_node()
            
        for link in self.links:
            aimnodes.link(link[0], link[1], link[2])

        aimnodes.end_node_editor()

        if (result := aimnodes.is_link_created(0,0))[0]:
            print('output:  ', result[1])
            print('input:  ', result[2])
            self.add_link(result[1], result[2])

        if (result := aimnodes.is_link_destroyed(0))[0]:
            print(result[1])

        aimgui.end()
        #aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()
    '''
app = App()

arcade.run()
