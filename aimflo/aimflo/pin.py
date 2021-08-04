import aimgui
import aimnodes

class Pin:
    id_counter = 0

    def __init__(self, node, name):
        self.id = self.id_counter
        self.id_counter += 1
        self.node = node
        self.name = name
        self.wires = []
        self.x = 0
        self.y = 0

    def add_wire(self, wire):
        self.wires.append(wire)

    def set_position(self, pos):
        self.x, self.y = pos

    def get_position(self):
        return (self.x, self.y)

    def draw(self):
        self.begin()
        self.end()

    def begin(self):
        pass

    def end(self):
        pass

class Input(Pin):
    def __init__(self, node, name, action):
        super().__init__(node, name)
        self.action = action

    def add_wire(self, wire):
        super().add_wire(wire)
        wire.output.observable.subscribe(self.action)

    def begin(self):
        aimnodes.begin_input_attribute(self.id)
        aimgui.text(self.name)

    def end(self):
        aimnodes.end_input_attribute()

class Output(Pin):
    def __init__(self, node, name, observable):
        super().__init__(node, name)
        self.observable = observable

    def write(self, value):
        self.observable.on_next(value)

    def begin(self):
        aimnodes.begin_output_attribute(self.id)
        aimgui.text(self.name)

    def end(self):
        aimnodes.end_output_attribute()
