import aimgui as gui

from aimdemo.page import Page


class DragFloat(Page):
    def reset(self):
        self.value = 42.0

    def draw(self):
        gui.begin("Example: drag float")
        changed, self.value = gui.drag_float(
            "Default", self.value,
        )
        changed, self.value = gui.drag_float(
            "Less precise", self.value, format="%.1f"
        )
        gui.text("Changed: %s, Value: %s" % (changed, self.value))
        gui.end()

class DragFloat2(Page):
    def reset(self):
        self.values = 88.0, 42.0

    def draw(self):
        gui.begin("Example: drag float 2")
        changed, self.values = gui.drag_float2(
            "Default", self.values
        )
        changed, self.values = gui.drag_float2(
            "Less precise", self.values, format="%.1f"
        )
        gui.text("Changed: %s, Values: %s" % (changed, self.values))
        gui.end()

class DragFloat3(Page):
    def reset(self):
        self.values = 88.0, 42.0, 69.0

    def draw(self):
        gui.begin("Example: drag float 3")
        changed, self.values = gui.drag_float3(
            "Default", self.values
        )
        changed, self.values = gui.drag_float3(
            "Less precise", self.values, format="%.1f"
        )
        gui.text("Changed: %s, Values: %s" % (changed, self.values))
        gui.end()

class DragFloat4(Page):
    def reset(self):
        self.values = 88.0, 42.0, 69.0, 0.0

    def draw(self):
        gui.begin("Example: drag float 4")
        changed, self.values = gui.drag_float4(
            "Default", self.values
        )
        changed, self.values = gui.drag_float4(
            "Less precise", self.values, format="%.1f"
        )
        gui.text("Changed: %s, Values: %s" % (changed, self.values))
        gui.end()

def install(app):
    app.add_page(DragFloat, "dragfloat", "Drag Float")
    app.add_page(DragFloat2, "dragfloat2", "Drag Float 2")
    app.add_page(DragFloat3, "dragfloat3", "Drag Float 3")
    app.add_page(DragFloat4, "dragfloat4", "Drag Float 4")
