import aimgui
from aimgui.impl.aimgfx import AimGfxGui

import aimgfx
from aimgfx.window import Window
from aimgfx.constants import *

import python_image

class ImGui(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.gui = AimGfxGui(self)
        aimgui.set_next_window_pos( (16, 32) )
        aimgui.set_next_window_size( (512, 512) )

        self.init_conf = aimgfx.Init()
        self.init_conf.debug = True
        self.init_conf.resolution.width = self.width
        self.init_conf.resolution.height = self.height
        self.init_conf.resolution.reset = BGFX_RESET_VSYNC

    def init(self, platform_data):
        aimgfx.render_frame()
        aimgfx.set_platform_data(platform_data)
        aimgfx.init(self.init_conf)

        aimgfx.set_debug(BGFX_DEBUG_TEXT)
        aimgfx.set_view_clear(0, BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH, 0x443355FF, 1.0, 0)

    def shutdown(self):
        aimgfx.shutdown()

    def update(self, dt):
        mouse_x, mouse_y, buttons_states = self.get_mouse_state()

        aimgfx.set_view_rect(0, 0, 0, self.width, self.height)
        aimgfx.touch(0)
        aimgfx.dbg_text_clear(0, False)
        aimgfx.dbg_text_image(
            int(max(self.width / 2 / 8, 20)) - 20,
            int(max(self.height / 2 / 16, 6)) - 6,
            40,
            12,
            python_image.logo,
            160,
        )

        stats = aimgfx.get_stats()

        aimgfx.dbg_text_printf(
            1,
            1,
            0x0F,
            "Color can be changed with ANSI \x1b[9;me\x1b[10;ms\x1b[11;mc\x1b[12;ma\x1b[13;mp\x1b[14;me\x1b[0m code too.",
        )
        aimgfx.dbg_text_printf(
            80,
            1,
            0x0F,
            "\x1b[;0m    \x1b[;1m    \x1b[; 2m    \x1b[; 3m    \x1b[; 4m    \x1b[; 5m    \x1b[; 6m    \x1b[; 7m    \x1b[0m",
        )
        aimgfx.dbg_text_printf(
            80,
            2,
            0x0F,
            "\x1b[;8m    \x1b[;9m    \x1b[;10m    \x1b[;11m    \x1b[;12m    \x1b[;13m    \x1b[;14m    \x1b[;15m    \x1b[0m",
        )
        aimgfx.dbg_text_printf(
            1,
            2,
            0x0F,
            f"Backbuffer {stats.width}W x {stats.height}H in pixels, debug text {stats.text_width}W x {stats.text_height}H in characters.",
        )

        aimgui.new_frame()

        aimgui.begin("Example: button")
        aimgui.button("Button 1")
        aimgui.button("Button 2")
        aimgui.end()

        aimgui.end_frame()

        self.gui.render()

        aimgfx.frame()

    def resize(self, width, height):
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format
        )


def main():
    test = ImGui(1280, 720, "examples/imgui")
    test.run()

if __name__ == "__main__":
    main()