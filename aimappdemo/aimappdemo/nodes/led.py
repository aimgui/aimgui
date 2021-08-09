from array import array
from random import random
from math import sin

import aimgui
import aimnodes

from aimflo.node import Node
from aimflo.pin import Input

class LedNode(Node):
    def __init__(self, graph, name):
        super().__init__(graph, name)
        self.value = 0
        self.input = Input(self, 'input', self.process)

    def process(self, value):
        self.value = value

    def begin(self):
        super().begin()
        aimgui.text(str(self.value))

