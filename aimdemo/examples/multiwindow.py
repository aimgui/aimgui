import aimgui as gui
from aimgui.renderers.arcade import ArcadeRenderer

import arcade

class ChildGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        self.context = gui.create_context()
        self.renderer = ArcadeRenderer(window)
        gui.set_next_window_pos( (16, 32) )
        gui.set_next_window_size( (512, 512) )

    def draw(self):
        #gui.set_current_context(self.context)
        gui.new_frame()


        gui.begin("Child")
        gui.button("Button 1")
        gui.button("Button 2")
        gui.end()

        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class ChildApp(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Child Window", resizable=True)
        self.gui = ChildGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        self.context = gui.create_context()
        self.renderer = ArcadeRenderer(window)
        gui.set_next_window_pos( (16, 32) )
        gui.set_next_window_size( (512, 512) )

    def draw(self):
        #gui.set_current_context(self.context)
        gui.new_frame()


        gui.begin("Parent")
        gui.button("Button 1")
        gui.button("Button 2")
        gui.end()

        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = MyGui(self)
        io = gui.get_io()
        io.config_flags |= gui.CONFIG_FLAGS_DOCKING_ENABLE | gui.CONFIG_FLAGS_VIEWPORTS_ENABLE

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = ChildApp()
app = App()
arcade.run()
