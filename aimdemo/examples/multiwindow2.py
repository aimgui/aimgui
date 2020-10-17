import aimgui
from aimgui.impl.arcade import ArcadeGui
#from aimgui.impl.arcade import ArcadeRenderer
'''
class ArcadeGui:
    def __init__(self, window, shared=False):
        self.shared = shared
        self.window = window
        # Must create or set the context before instantiating the renderer
        if not shared:
            self.context = aimgui.create_context()
        else:
            print('shared')
            self.context = aimgui.get_current_context()

        self.renderer = ArcadeRenderer(window)

    def push_portal(self, draw_list, portal):
        def cb(renderer, draw_data, draw_list, cmd, user_data):
            renderer.push_portal(portal)
        draw_list.add_callback(cb, None)

    def pop_portal(self, draw_list):
        def cb(renderer, draw_data, draw_list, cmd, user_data):
            renderer.pop_portal()
        draw_list.add_callback(cb, None)

    def draw(self):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())

    def update(self, delta_time):
        aimgui.render()
        self.renderer.render(aimgui.get_draw_data())
'''
import arcade

class ChildGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window, True)
        self.title = "Child Gui"
        io = aimgui.get_io()
        #io.config_flags |= aimgui.CONFIG_FLAGS_DOCKING_ENABLE | aimgui.CONFIG_FLAGS_VIEWPORTS_ENABLE

    def draw(self):
        #print(self.context)
        #io = aimgui.get_io()
        #print(io.display_size)
        #aimgui.set_current_context(self.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )
        aimgui.begin('Dockable Window#1')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()

        aimgui.end_frame()

        super().draw()

class ChildApp(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Child Window", resizable=True)
        self.gui = ArcadeGui(self)

    def on_draw(self):
        arcade.start_render()
        print(self.gui.context)
        aimgui.set_current_context(self.gui.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )
        aimgui.begin('Dockable Window#1')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()

        aimgui.end_frame()

        self.gui.draw()

class MyGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window)
        self.title = "Parent Gui"
        io = aimgui.get_io()
        #io.config_flags |= aimgui.CONFIG_FLAGS_DOCKING_ENABLE | aimgui.CONFIG_FLAGS_VIEWPORTS_ENABLE

    def draw(self):
        #aimgui.set_current_context(self.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size( (512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Dockable Window#2')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()
        aimgui.show_metrics_window()
        aimgui.end_frame()

        super().draw()

class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Main Window", resizable=True)
        self.gui = ArcadeGui(self)

    def on_draw(self):
        arcade.start_render()
        print(self.gui.context)
        aimgui.set_current_context(self.gui.context)
        aimgui.new_frame()

        aimgui.set_next_window_pos( (16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size( (512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin('Dockable Window#2')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()
        aimgui.show_metrics_window()
        aimgui.end_frame()
        self.gui.draw()

app = App()
app = ChildApp()

arcade.run()
import pyglet
#pyglet.app.run()
