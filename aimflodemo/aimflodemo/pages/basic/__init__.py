import arcade
import aimgui
import aimnodes

from aimflodemo.page import Page

from .volume import VolumeNode
from .led import LedNode
from aimflo.wire import Wire

class BasicPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        self.nodes = []
        self.wires = []
        volume_node = VolumeNode('Volume')
        led_node = LedNode('Led')
        self.add_node(volume_node)
        self.add_node(led_node)
        self.add_wire(Wire(volume_node.get_pin('output'), led_node.get_pin('input')))

    def draw(self):
        aimgui.begin('Node Editor')
        aimnodes.begin_node_editor()
        for node in self.nodes:
            node.draw()
        aimnodes.end_node_editor()

        for wire in self.wires:
            wire.draw()
        aimgui.end()

def install(app):
    app.add_page(BasicPage, "basic", "Basic")
