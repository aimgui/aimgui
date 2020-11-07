import moderngl_window
from pyrr import Matrix44

import aimgui
from aimgui.impl.moderngl import ModernGLGui


class App(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    title = "Button Example"
    #resource_dir = (Path(__file__).parent / 'resources').resolve()
    aspect_ratio = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gui = ModernGLGui(self.wnd)

    def render(self, time: float, frametime: float):

        aimgui.new_frame()

        aimgui.set_next_window_pos((16, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((512, 512), aimgui.COND_ONCE)

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        aimgui.end()

        aimgui.end_frame()

        self.gui.render()

    def resize(self, width: int, height: int):
        self.gui.resize(width, height)

    def key_event(self, key, action, modifiers):
        self.gui.key_event(key, action, modifiers)

    def mouse_position_event(self, x, y, dx, dy):
        self.gui.mouse_position_event(x, y, dx, dy)

    def mouse_drag_event(self, x, y, dx, dy):
        self.gui.mouse_drag_event(x, y, dx, dy)

    def mouse_scroll_event(self, x_offset, y_offset):
        self.gui.mouse_scroll_event(x_offset, y_offset)

    def mouse_press_event(self, x, y, button):
        self.gui.mouse_press_event(x, y, button)

    def mouse_release_event(self, x: int, y: int, button: int):
        self.gui.mouse_release_event(x, y, button)

    def unicode_char_entered(self, char):
        self.gui.unicode_char_entered(char)


moderngl_window.run_window_config(App)