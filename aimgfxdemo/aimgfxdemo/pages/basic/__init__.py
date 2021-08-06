import arcade
import aimgui
import aimnodes

from aimflo.page import Page

from aimflodemo.nodes.volume import VolumeNode
from aimflodemo.nodes.led import LedNode
from aimflo.wire import Wire

class BasicPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        volume_node = VolumeNode(self.graph, 'Volume')
        led_node = LedNode(self.graph, 'Led')
        self.graph.add_wire(Wire(volume_node.get_pin('output'), led_node.get_pin('input')))

def install(app):
    app.add_page(BasicPage, "basic", "Basic")
