import aimgui as gui
from aimgui.renderers.arcade import ArcadeRenderer

import arcade

class ChildGui:
    def __init__(self, window):
        self.window = window
        self.title = "Child Gui"
        # Must create or set the context before instantiating the renderer
        self.context = gui.create_context()
        io = gui.get_io()
        #io.config_flags |= gui.CONFIG_FLAGS_DOCKING_ENABLE | gui.CONFIG_FLAGS_VIEWPORTS_ENABLE

        self.renderer = ArcadeRenderer(window)

    def draw(self):
        #gui.set_current_context(self.context)
        gui.new_frame()

        gui.set_next_window_pos((16, 32), gui.COND_FIRST_USE_EVER )
        gui.set_next_window_size( (512, 512), gui.COND_FIRST_USE_EVER )


        #gui.begin(self.title)

        #dockspace_id = gui.get_id(self.title)
        #dockspace_flags = gui.DOCK_NODE_FLAGS_NONE|gui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #gui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        #gui.end()


        #gui.set_next_window_dock_id(dockspace_id , gui.COND_FIRST_USE_EVER)


        gui.begin('Dockable Window#1')
        gui.begin_child("region", (150, -50), border=True)
        gui.text("inside region")
        gui.end_child()
        gui.text("outside region")
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
        self.title = "Parent Gui"
        # Must create or set the context before instantiating the renderer
        self.context = gui.create_context()
        io = gui.get_io()
        #io.config_flags |= gui.CONFIG_FLAGS_DOCKING_ENABLE | gui.CONFIG_FLAGS_VIEWPORTS_ENABLE
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        #gui.set_current_context(self.context)
        gui.new_frame()

        gui.set_next_window_pos( (16, 32), gui.COND_FIRST_USE_EVER )
        gui.set_next_window_size( (512, 512), gui.COND_FIRST_USE_EVER )

        #gui.begin(self.title)

        #dockspace_id = gui.get_id(self.title)
        #dockspace_flags = gui.DOCK_NODE_FLAGS_NONE|gui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #gui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        #gui.end()


        #gui.set_next_window_dock_id(dockspace_id , gui.COND_FIRST_USE_EVER)


        gui.begin('Dockable Window#2')
        gui.begin_child("region", (150, -50), border=True)
        gui.text("inside region")
        gui.end_child()
        gui.text("outside region")
        gui.end()
        gui.show_metrics_window()
        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
app = ChildApp()

arcade.run()
