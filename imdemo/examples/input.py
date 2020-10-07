import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        # Window variables
        self.test_input = 0

    def draw(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        imgui.begin("Test Window")
        imgui.text("This is the test window.")
        changed, self.test_input = imgui.input_int("Integer Input Test", self.test_input)

        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Input Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()
        arcade.draw_text(str(self.gui.test_input), 128, 128, arcade.color.WHITE_SMOKE, 64)


app = App()
arcade.run()
