import arcade
import aimgui

from aimdemo.page import Page


class Input(Page):
    def reset(self):
        self.test_input = 0

    def draw(self):
        aimgui.begin(self.title)

        aimgui.text("This is the test window.")
        changed, self.test_input = aimgui.input_int("Integer", self.test_input)

        aimgui.end()

        arcade.draw_text(str(self.test_input), 0, 0, arcade.color.WHITE_SMOKE, 64)

class InputDouble(Page):
    def reset(self):
        self.double_val = 3.14159265358979323846

    def draw(self):
        aimgui.begin("Test Window")

        aimgui.text("This is the test window.")
        changed, self.double_val = aimgui.input_double('Double:', self.double_val)
        aimgui.text('You wrote: %d' % self.double_val)

        aimgui.end()

        arcade.draw_text(str(self.double_val), 0, 0, arcade.color.WHITE_SMOKE, 64)

class InputFloat(Page):
    def reset(self):
        self.float_val = 0.4

    def draw(self):
        aimgui.begin("Test Window")

        aimgui.text("This is the test window.")
        changed, self.float_val = aimgui.input_float('Float:', self.float_val)
        aimgui.text('You wrote: %f' % self.float_val)
        aimgui.end()

        arcade.draw_text(str(self.float_val), 0, 0, arcade.color.WHITE_SMOKE, 64)

def install(app):
    app.add_page(Input, "input", "Input")
    app.add_page(InputDouble, "inputdouble", "Input Double")
    app.add_page(InputFloat, "inputfloat", "Input Float")
