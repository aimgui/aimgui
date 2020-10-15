from array import array
from random import random
from math import sin

import arcade
import aimgui as gui

from aimflo.node import Node
from aimflo.pin import Input

class LedNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self.value = 0
        self.input = Input(self, 'input', self.process)
        self.add_pin(self.input)

    def process(self, value):
        self.value = value

    def draw(self):
        #gui.set_next_window_position(self.window.width - 256 - 16, 32, gui.COND_ONCE)
        #gui.set_next_window_size(256, 256, gui.COND_ONCE)

        gui.begin("Led")

        self.begin_input(self.input)
        gui.button('input')
        self.end_input()

        gui.same_line(spacing=16)
        gui.text(str(self.value))
        gui.end()

