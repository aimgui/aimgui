import arcade

import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        imgui.show_test_window()

        imgui.begin("Custom window", True)
        imgui.text("Bar")
        imgui.text_colored("Eggs", 0.2, 1., 0.)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "Arcade Imgui Test", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
