import arcade
import aimgui as gui

from aimflo.page import Page

from .volume import VolumeNode
from .led import LedNode
from aimflo.wire import Wire

class ConnectPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        volume_node = self.add_node(VolumeNode(self))
        led_node = self.add_node(LedNode(self))

def install(app):
    app.add_page(ConnectPage, "connect", "Connect")
