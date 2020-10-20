import arcade
import aimgui

from aimgui.impl.arcade import ArcadeGui

SPRITE_SCALING = 0.5
FBSIZE = (512, 256)

class MyGui(ArcadeGui):
    def __init__(self, window):
        super().__init__(window)
        self.sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_orange.png",
            SPRITE_SCALING,
            center_x = 256,
            center_y = 128
            )
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(image.size, components=3, data=image.convert("RGB").tobytes())
        self.offscreen = window.ctx.framebuffer(color_attachments=window.ctx.texture(FBSIZE))
        self.reset()

    def reset(self):
        self.rotation = 0
        self.scale = 1
        self.alpha = 255
        self.color_enabled = True
        self.color = 1,1,1

    def draw(self):
        aimgui.new_frame()

        #gui.set_next_window_pos(self.window.width - 256 - 16, 32, aimgui.COND_ONCE)
        aimgui.set_next_window_size((512, 512), aimgui.COND_ONCE)

        aimgui.begin("Framebuffer Example")

        # Rotation
        aimgui.image(self.texture.glo.value, self.texture.size)
        
        changed, self.rotation = aimgui.drag_float(
            "Rotation", self.rotation,
        )
        self.sprite.angle = self.rotation

        # Scale
        changed, self.scale = aimgui.drag_float(
            "Scale", self.scale, .1
        )
        self.sprite.scale = self.scale

        # Alpha
        changed, self.alpha = aimgui.drag_int(
            "Alpha", self.alpha, 1, 0, 255
        )
        self.sprite.alpha = self.alpha

        # Color
        _, self.color_enabled = aimgui.checkbox("Tint", self.color_enabled)
        if self.color_enabled:
            changed, self.color = aimgui.color_edit3("Color", self.color)
            self.sprite.color = (int(self.color[0] * 255), int(self.color[1] * 255), int(self.color[2] * 255))
        else:
            self.sprite.color = 255, 255, 255

        if aimgui.button("Reset"):
            self.reset()

        fbtexture = self.offscreen.color_attachments[0]
        aimgui.image(fbtexture.glo.value, FBSIZE)

        aimgui.end()

        self.offscreen.use()
        self.offscreen.clear((0, 0, 0, 0))
        vp = arcade.get_viewport()
        arcade.set_viewport(0, FBSIZE[0], 0, FBSIZE[1])
        prj = self.window.ctx.projection_2d
        self.window.ctx.projection_2d = (0, FBSIZE[0],FBSIZE[1],0)
        self.sprite.draw()
        arcade.draw_text("Simple line of text in 20 point", 0,0 , arcade.color.WHITE, 20)

        self.window.ctx.projection_2d = prj

        self.window.use()
        arcade.set_viewport(*vp)
        self.sprite.draw()

        aimgui.end_frame()

        super().draw()

class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Framebuffer Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
