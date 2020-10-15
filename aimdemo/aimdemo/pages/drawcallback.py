import arcade

import aimgui

from aimdemo.page import Page


class DrawCallbackPage(Page):
    def draw(self):
        aimgui.begin(self.title)

        draw_list = aimgui.get_window_draw_list()

        def draw_text(draw_data, draw_list, cmd, user_data):
            vp = self.window.get_viewport()
            clip = cmd.clip_rect
            left = clip[0]
            bottom = self.window.height - clip[3]

            #Clipping rectangle (x1, y1, x2, y2). Subtract ImDrawData->DisplayPos to get clipping rectangle in "viewport" coordinates
            arcade.draw_text("Simple line of text in 20 point", left, bottom, arcade.color.WHITE, 20)

        draw_list.add_callback(draw_text, None)

        aimgui.end()

def install(app):
    app.add_page(DrawCallbackPage, "drawcallback", "Draw Callback")
