import aimgui
from aimgui.renderers.arcade import ArcadeRenderer

import arcade

class ChildGui:
    def __init__(self, window):
        self.window = window
        self.title = "Child Gui"
        # Must create or set the context before instantiating the renderer
        self.context = aimgui.create_context()
        io = aimgui.get_io()
        #io.config_flags |= aimgui.CONFIG_FLAGS_DOCKING_ENABLE | aimgui.CONFIG_FLAGS_VIEWPORTS_ENABLE

        self.renderer = ArcadeRenderer(window)

    def draw(self):
        #gui.set_current_context(self.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size( (512, 512), aimgui.COND_FIRST_USE_EVER )


        #gui.begin(self.title)

        #dockspace_id = aimgui.get_id(self.title)
        #dockspace_flags = aimgui.DOCK_NODE_FLAGS_NONE|aimgui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #gui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        #gui.end()


        #gui.set_next_window_dock_id(dockspace_id , aimgui.COND_FIRST_USE_EVER)


        aimgui.begin('Dockable Window#1')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()

        aimgui.end_frame()

        aimgui.render()

        self.renderer.render(aimgui.get_draw_data())


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
        self.context = aimgui.create_context()
        io = aimgui.get_io()
        #io.config_flags |= aimgui.CONFIG_FLAGS_DOCKING_ENABLE | aimgui.CONFIG_FLAGS_VIEWPORTS_ENABLE
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        #gui.set_current_context(self.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size( (512, 512), aimgui.COND_FIRST_USE_EVER )

        #gui.begin(self.title)

        #dockspace_id = aimgui.get_id(self.title)
        #dockspace_flags = aimgui.DOCK_NODE_FLAGS_NONE|aimgui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #gui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        #gui.end()


        #gui.set_next_window_dock_id(dockspace_id , aimgui.COND_FIRST_USE_EVER)


        aimgui.begin('Dockable Window#2')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()
        aimgui.show_metrics_window()
        aimgui.end_frame()

        aimgui.render()

        self.renderer.render(aimgui.get_draw_data())


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
