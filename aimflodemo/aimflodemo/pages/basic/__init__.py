import arcade
import aimgui
import aimnodes

from aimflo.page import Page

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

def install(app):
    app.add_page(BasicPage, "basic", "Basic")
