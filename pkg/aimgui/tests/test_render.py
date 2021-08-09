import arcade
import aimgui
import aimgui

from aimgui.renderers.arcade import ArcadeRenderer

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

        aimgui.begin("Example: bullets")

        for i in range(10):
            aimgui.bullet()

        aimgui.end()

        aimgui.end_frame()

        aimgui.render()

        self.renderer.render(aimgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "Test Render")
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


def test_render():
    app = App()
    app.on_draw()