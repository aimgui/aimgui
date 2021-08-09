import arcade
import aimgui

from aimflo.page import Page

from aimflodemo.nodes.volume import VolumeNode
from aimflodemo.nodes.led import LedNode

class ConnectPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        VolumeNode(self.graph, 'Volume')
        LedNode(self.graph, 'Led')

def install(app):
    app.add_page(ConnectPage, "connect", "Connect")
