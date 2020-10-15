from rx.subject import Subject

import arcade
import aimgui as gui

from aimflo.node import Node
from aimflo.pin import Output

class VolumeNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self._value = 88
        self.subject = Subject()
        self.output = Output(self, 'output', self.subject)
        self.add_pin(self.output)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.output.write(value)

    def draw(self):
        width = 20
        height = 100

        gui.set_next_window_size((160, 160), gui.COND_ONCE)

        gui.begin("Volume")

        changed, self.value = gui.v_slider_int(
            "volume",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%d"
        )
        gui.same_line(spacing=16)
        self.begin_output(self.output)
        gui.button('output')
        self.end_output()

        gui.end()

