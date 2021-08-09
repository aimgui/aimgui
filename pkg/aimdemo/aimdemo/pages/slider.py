import aimgui

from aimdemo.page import Page


class FloatSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        aimgui.begin(self.title)
        changed, self.value = aimgui.v_slider_float(
            "vertical slider float",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%0.3f"
        )
        aimgui.text("Changed: %s, Values: %s" % (changed, self.value))
        aimgui.end()

class IntSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        aimgui.begin(self.title)
        changed, self.value = aimgui.v_slider_int(
            "vertical slider int",
            (width, height), self.value,
            v_min=0, v_max=100,
            format="%d"
        )
        aimgui.text("Changed: %s, Values: %s" % (changed, self.value))
        aimgui.end()

def install(app):
    app.add_page(FloatSliderPage, "floatslider", "Slider - Float")
    app.add_page(IntSliderPage, "intslider", "Slider - Integer")
