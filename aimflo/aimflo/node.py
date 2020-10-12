import arcade
import aimgui as gui

class Node:
    def __init__(self, page):
        self.page = page
        self.pins = {}

    def reset(self):
        pass

    def add_pin(self, pin):
        self.pins[pin.name] = pin

    def get_pin(self, name):
        return self.pins[name]

    def begin_input(self, pin):
        x, y = gui.get_cursor_screen_pos()
        wx, wy = gui.get_window_pos()
        x = wx - 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def end_input(self):
        if gui.begin_drag_drop_target():
            payload = gui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                payload = self.page.end_dnd()
                print('Received:', payload)
                self.page.connect(payload, self.input)
            gui.end_drag_drop_target()

    def begin_output(self, pin):
        x, y = gui.get_cursor_screen_pos()
        wx, wy = gui.get_window_pos()
        ww, wh = gui.get_window_size()

        x = wx + ww + 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def end_output(self):
        if gui.begin_drag_drop_source():
            gui.set_drag_drop_payload('itemtype', b'payload')
            self.page.start_dnd(self.output)
            gui.button('dragged source')
            gui.end_drag_drop_source()

    def update(self, delta_time):
        pass

    def draw(self):
        pass