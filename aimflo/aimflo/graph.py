import arcade
import aimgui
import aimnodes

from aimflo.wire import Wire

class Graph:
    def __init__(self):
        self.nodes = []
        self.node_map = {}
        self.wires = []
        self.wire_map = {}
        self.pins = []
        self.pin_map = {}

    def reset(self):
        for node in self.nodes:
            node.reset()

    def add_node(self, node):
        node.graph = self
        self.nodes.append(node)
        self.node_map[node.id] = node
        return node

    def remove_node(self, node):
        self.nodes.remove(node)
        self.node_map.pop(node.id)

    def add_wire(self, wire):
        self.wires.append(wire)
        self.wire_map[wire.id] = wire

    def remove_wire(self, wire):
        wire.destroy()
        self.wires.remove(wire)
        self.wire_map.pop(wire.id)

    def add_pin(self, pin):
        self.pins.append(pin)
        self.pin_map[pin.id] = pin

    def remove_pin(self, pin):
        pin.destroy()
        self.pins.remove(pin)
        self.pin_map.pop(pin.id)

    def connect(self, output, input):
        self.add_wire(Wire(output, input))

    def disconnect(self, wire):
        self.remove_wire(wire)

    def update(self, delta_time):
        for node in self.nodes:
            node.update(delta_time)

    def draw(self):
        aimgui.begin('Node Editor')
        aimnodes.begin_node_editor()
        for node in self.nodes:
            node.draw()
        for wire in self.wires:
            wire.draw()
        aimnodes.end_node_editor()

        if (result := aimnodes.is_link_created(0,0))[0]:
            print(result)
            output = self.pin_map[result[1]]
            input = self.pin_map[result[2]]
            print('output:  {output}')
            print('input:  {input}')
            self.connect(output, input)

        if (result := aimnodes.is_link_destroyed(0))[0]:
            wire = self.wire_map[result[1]]
            print('destroyed: ', wire)
            self.disconnect(wire)

        aimgui.end()
