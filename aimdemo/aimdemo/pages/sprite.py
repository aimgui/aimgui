import arcade
import aimgui as gui

from aimdemo.page import Page

SPRITE_SCALING = 0.5


class SpritePage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        self.sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_orange.png",
            SPRITE_SCALING,
            center_x = 512,
            center_y = 256
            )
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(image.size, components=3, data=image.convert("RGB").tobytes())

    def reset(self):
        self.rotation = 0
        self.scale = 1
        self.alpha = 255
        self.color_enabled = True
        self.color = 1,1,1

    def draw(self):
        #gui.set_next_window_position(288, 32, gui.ONCE)
        gui.set_next_window_pos((self.window.width - 256 - 16, 32), gui.ONCE)
        gui.set_next_window_size((256, 256), gui.ONCE)

        gui.begin("Ship")

        # Rotation
        gui.image(self.texture.glo.value, self.texture.size)
        changed, self.rotation = gui.drag_float(
            "Rotation", self.rotation,
        )
        self.sprite.angle = self.rotation

        # Scale
        changed, self.scale = gui.drag_float(
            "Scale", self.scale, .1
        )
        self.sprite.scale = self.scale

        # Alpha
        changed, self.alpha = gui.drag_int(
            "Alpha", self.alpha, 1, 0, 255
        )
        self.sprite.alpha = self.alpha

        # Color
        _, self.color_enabled = gui.checkbox("Tint", self.color_enabled)
        if self.color_enabled:
            changed, self.color = gui.color_edit3("Color", self.color)
            self.sprite.color = (int(self.color[0] * 255), int(self.color[1] * 255), int(self.color[2] * 255))
        else:
            self.sprite.color = 255, 255, 255

        if gui.button("Reset"):
            self.reset()

        gui.end()

        self.sprite.draw()

def install(app):
    app.add_page(SpritePage, "sprite", "Sprite")
