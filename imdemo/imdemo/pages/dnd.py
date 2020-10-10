import aimgui as gui

from imdemo.page import Page


class DnD(Page):
    def draw(self):
        gui.begin("Example: drag and drop")

        gui.button('source')
        if gui.begin_drag_drop_source():
            gui.set_drag_drop_payload('itemtype', b'payload')
            gui.button('dragged source')
            gui.end_drag_drop_source()

        gui.button('dest')
        if gui.begin_drag_drop_target():
            payload = gui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                print('Received:', payload)
            gui.end_drag_drop_target()

        gui.end()

def install(app):
    app.add_page(DnD, "dnd", "Drag & Drop")
