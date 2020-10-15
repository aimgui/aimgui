import aimgui
from aimgui.renderers.arcade import ArcadeRenderer

import arcade


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        aimgui.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32) )
        aimgui.set_next_window_size( (512, 512) )

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        aimgui.end()

        aimgui.end_frame()

        aimgui.render()

        self.renderer.render(aimgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Button Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
