import time
from math import sin
import numpy as np
from rx.subject import Subject

import aimgui

from aimflo.node import Node
from aimflo.pin import Output

sampling_rate = 44100
freq = 440
samples = 44100
#x = np.arange(samples)
#y = 100*np.sin(2 * np.pi * freq * x / sampling_rate)

class SineNode(Node):
    def __init__(self, graph, name):
        super().__init__(graph, name)
        self._freq = 88
        self.clock = 0
        self.subject = Subject()
        self.output = Output(self, 'output', self.subject)

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        self._freq = value

    def update(self, delta_time):
        self.clock = self.clock + delta_time
        x = self.clock
        y = np.sin(self.freq * x)
        self.output.write(y)
    
    def begin(self):
        super().begin()
        width = 20
        height = 100

        changed, freq = aimgui.v_slider_int(
            "freq",
            (width, height), self.freq,
            v_min=0, v_max=100,
            format="%d"
        )
        if changed:
            self.freq = freq
