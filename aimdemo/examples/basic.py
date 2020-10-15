import aimgui
from aimgui.impl.arcade import ArcadeGui

import arcade

class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Button Example", resizable=True)
        self.gui = ArcadeGui(self)

    def on_draw(self):
        arcade.start_render()

        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32) )
        aimgui.set_next_window_size( (512, 512) )

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        aimgui.end()

        aimgui.end_frame()

        self.gui.draw()


app = App()
arcade.run()
