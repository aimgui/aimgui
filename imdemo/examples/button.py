import aimgui as gui
from aimgui.renderers.arcade import ArcadeRenderer

import arcade


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        gui.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        gui.new_frame()

        gui.set_next_window_pos( (16, 32) )
        gui.set_next_window_size( (512, 512) )

        gui.begin("Example: button")
        gui.button("Button 1")
        gui.button("Button 2")
        gui.end()

        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Button Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
