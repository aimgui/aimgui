import arcade

import aimgui

from aimdemo.page import Page


class DrawCallbackPage(Page):
    def draw(self):
        aimgui.begin(self.title)

        def draw_text(renderer, draw_data, draw_list, cmd, user_data):
            clip = cmd.clip_rect
            left = clip[0]
            bottom = self.window.height - clip[3]

            arcade.draw_text("Simple line of text in 20 point", left, bottom, arcade.color.WHITE, 20)

        draw_list = aimgui.get_window_draw_list()

        draw_list.add_callback(draw_text, None)

        aimgui.end()

def install(app):
    app.add_page(DrawCallbackPage, "drawcallback", "Draw Callback")
