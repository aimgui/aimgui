from rx.subject import Subject

import arcade
import aimgui

from aimflo.node import Node
from aimflo.pin import Output

class VolumeNode(Node):
    def __init__(self, graph, name):
        super().__init__(graph, name)
        self._value = 88
        self.subject = Subject()
        self.output = Output(self, 'output', self.subject)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.output.write(value)

    def begin(self):
        super().begin()
        width = 20
        height = 100
        changed, self.value = aimgui.v_slider_int(
            "volume",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%d"
        )

