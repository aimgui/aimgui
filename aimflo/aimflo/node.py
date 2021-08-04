import arcade
import aimgui
import aimnodes

class Node:
    id_counter = 0
    def __init__(self, graph, name):
        self.graph = graph
        self.id = Node.id_counter
        Node.id_counter += 1
        self.name = name
        self.page = None
        self.pins = []
        self.pin_map = {}
        self.graph.add_node(self)

    def reset(self):
        pass

    def add_pin(self, pin):
        self.graph.add_pin(pin)
        self.pins.append(pin)
        self.pin_map[pin.name] = pin

    def get_pin(self, name):
        return self.pin_map[name]

    def update(self, delta_time):
        pass

    def draw(self):
        self.begin()
        self.end()

    def begin(self):
        aimnodes.begin_node(self.id)
        aimnodes.begin_node_title_bar()
        aimgui.text(self.name)
        aimnodes.end_node_title_bar()

    def end(self):
        for pin in self.pins:
            pin.draw()
        aimnodes.end_node()