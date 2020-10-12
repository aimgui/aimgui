from array import array
from collections import deque
from random import random
from math import sin
import numpy as np

import arcade
import aimgui as gui

from aimflo.node import Node
from aimflo.pin import Input

class ScopeNode(Node):
    def __init__(self, page):
        super().__init__(page)
        #self.values = array('f', [sin(x * 0.1) for x in range(100)])
        self.values = deque([0]*100, 100)
        self.input = Input(self, 'input', self.process)
        self.add_pin(self.input)

    def process(self, value):
        print(value)
        self.values.append(value)
        if len(self.values) > 100:
            self.values.popleft()

    def draw(self):
        gui.begin("Scope")
        self.begin_input(self.input)
        gui.button('input')
        self.end_input()
        gui.same_line(spacing=16)
        gui.plot_lines("Sin(t)", np.array(self.values).astype(np.float32), graph_size=gui.get_content_region_avail())

        gui.end()

