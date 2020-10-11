import aimgui as gui

from aimdemo.page import Page


class FloatSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        gui.begin(self.title)
        changed, self.value = gui.v_slider_float(
            "vertical slider float",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%0.3f"
        )
        gui.text("Changed: %s, Values: %s" % (changed, self.value))
        gui.end()

class IntSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        gui.begin(self.title)
        changed, self.value = gui.v_slider_int(
            "vertical slider int",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%d"
        )
        gui.text("Changed: %s, Values: %s" % (changed, self.value))
        gui.end()

def install(app):
    app.add_page(FloatSliderPage, "floatslider", "Slider - Float")
    app.add_page(IntSliderPage, "intslider", "Slider - Integer")
