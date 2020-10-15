import arcade
from arcade import Point, Vector
from arcade.utils import _Vec2  # bring in "private" class
import os
import random
import pyglet

import aimgui as gui

from aimdemo.page import Page
from aimdemo.particle import AnimatedAlphaParticle

SCREEN_TITLE = "Particle based fireworks"

CLOUD_TEXTURES = [
    arcade.make_soft_circle_texture(50, arcade.color.WHITE),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_GRAY),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_BLUE),
]

class CloudPage(Page):
    def reset(self):
        self.create_emitter()
        self.fullwidth=self.fullheight=False

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def create_emitter(self):
        self.emitter = arcade.Emitter(
            center_xy=(64, self.window.height/2),
            change_xy=(0.15, 0),
            emit_controller=arcade.EmitMaintainCount(60),
            particle_factory=lambda emitter: AnimatedAlphaParticle(
                filename_or_texture=random.choice(CLOUD_TEXTURES),
                change_xy=(_Vec2(arcade.rand_in_circle((0.0, 0.0), 0.04)) + _Vec2(0.1, 0)).as_tuple(),
                start_alpha=0,
                duration1=random.uniform(5.0, 10.0),
                mid_alpha=255,
                duration2=random.uniform(5.0, 10.0),
                end_alpha=0,
                center_xy=arcade.rand_in_circle((0.0, 0.0), 50)
            )
        )

    def update(self, delta_time):
        if self.emitter.center_x > self.window.width:
            self.emitter.center_x = 0
        self.emitter.update()

    def draw(self):
        #gui.set_next_window_pos((self.window.width - 288, 32), gui.COND_ONCE)
        #gui.set_next_window_size((256, 256), gui.COND_ONCE)

        gui.begin("Cloud")
        if gui.button("Reset"):
            self.reset()
        gui.end()

        self.emitter.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

def install(app):
    app.add_page(CloudPage, "cloud", "Cloud")
