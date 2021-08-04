import arcade
import aimgui
import aimnodes

class Node:
    id_counter = 0
    def __init__(self, name):
        self.id = Node.id_counter
        print(self.id)
        Node.id_counter += 1
        self.name = name
        self.page = None
        self.pins = []
        self.pin_map = {}

    def reset(self):
        pass

    def add_pin(self, pin):
        self.pins.append(pin)
        self.pin_map[pin.name] = pin

    def get_pin(self, name):
        return self.pin_map[name]

    def begin_input(self, pin):
        pass
        '''
        x, y = aimgui.get_cursor_screen_pos()
        wx, wy = aimgui.get_window_pos()
        x = wx - 8
        pos = (x, y)
        pin.set_position(pos)
        return pos
        '''
    def end_input(self):
        pass
        '''
        if aimgui.begin_drag_drop_target():
            payload = aimgui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                payload = self.page.end_dnd()
                print('Received:', payload)
                self.page.connect(payload, self.input)
            aimgui.end_drag_drop_target()
        '''
    def begin_output(self, pin):
        pass
        '''
        x, y = aimgui.get_cursor_screen_pos()
        wx, wy = aimgui.get_window_pos()
        ww, wh = aimgui.get_window_size()

        x = wx + ww + 8
        pos = (x, y)
        pin.set_position(pos)
        return pos
        '''
    def end_output(self):
        pass
        '''
        if aimgui.begin_drag_drop_source():
            aimgui.set_drag_drop_payload('itemtype', b'payload')
            self.page.start_dnd(self.output)
            aimgui.button('dragged source')
            aimgui.end_drag_drop_source()
        '''

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