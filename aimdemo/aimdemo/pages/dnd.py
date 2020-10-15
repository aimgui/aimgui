import aimgui

from aimdemo.page import Page


class DnD(Page):
    def draw(self):
        aimgui.begin("Example: drag and drop")

        aimgui.button('source')
        if aimgui.begin_drag_drop_source():
            aimgui.set_drag_drop_payload('itemtype', 'payload')
            aimgui.button('dragged source')
            aimgui.end_drag_drop_source()

        aimgui.button('dest')
        if aimgui.begin_drag_drop_target():
            payload = aimgui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                print('Received Payload:  ', payload)
                print('Received Payload Data:', payload.data)
            aimgui.end_drag_drop_target()

        aimgui.end()

def install(app):
    app.add_page(DnD, "dnd", "Drag & Drop")
