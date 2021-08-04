from array import array
from random import random
from math import sin

import aimgui
import aimnodes

from aimflo.node import Node
from aimflo.pin import Input

class LedNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.value = 0
        self.input = Input(self, 'input', self.process)
        self.add_pin(self.input)

    def process(self, value):
        self.value = value

    def begin(self):
        super().begin()
        aimgui.text(str(self.value))

