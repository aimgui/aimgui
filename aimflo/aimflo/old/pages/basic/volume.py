from rx.subject import Subject

import arcade
import aimgui

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

        aimgui.set_next_window_size((160, 160), aimgui.COND_ONCE)

        aimgui.begin("Volume")

        changed, self.value = aimgui.v_slider_int(
            "volume",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%d"
        )
        aimgui.same_line(spacing=16)
        self.begin_output(self.output)
        aimgui.button('output')
        self.end_output()

        aimgui.end()

