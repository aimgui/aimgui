from pyglet import gl, clock
from pyglet.window import key, mouse
from arcade.gl import BufferDescription, Context
import arcade

import aimgui
from aimgui.renderer import compute_framebuffer_scale
from aimgui.renderer.gl_base import OpenGLRendererBase


class ArcadeRenderer(OpenGLRendererBase):
    """
    A renderer using the arcade.gl module instead of PyOpenGL.
    This is using pyglet's OpenGL bindings instead.
    """

    VERTEX_SHADER_SRC = """
    #version 330
    uniform mat4 ProjMtx;
    uniform vec2 Portal;
    in vec2 Position;
    in vec2 UV;
    in vec4 Color;
    out vec2 Frag_UV;
    out vec4 Frag_Color;
    void main() {
        Frag_UV = UV;
        Frag_Color = Color;
        gl_Position = ProjMtx * vec4(Position.xy + Portal, 0, 1);
    }
    """

    FRAGMENT_SHADER_SRC = """
    #version 330
    uniform sampler2D Texture;
    in vec2 Frag_UV;
    in vec4 Frag_Color;
    out vec4 Out_Color;
    void main() {
        Out_Color = Frag_Color * texture(Texture, Frag_UV.st);
    }
    """

    def __init__(self, window, *args, **kwargs):
        self._window = window
        self._ctx: Context = window.ctx
        self._program = None
        self._vao = None
        self._vbo = None
        self._ibo = None
        self._font_texture = None
        #
        self.portal = (0,0)
        self.portal_stack = []
        #
        super().__init__()

    def push_portal(self, portal):
        self.portal_stack.append(self.portal)
        self.portal = portal
        self._program["Portal"] = self.portal

    def pop_portal(self):
        self.portal = self.portal_stack.pop(-1)
        self._program["Portal"] = self.portal

    def render(self, draw_data):
        io = self.io    

        display_width, display_height = io.display_size
        fb_scale = io.display_framebuffer_scale
        fb_width = int(display_width * fb_scale[0])
        fb_height = int(display_height * fb_scale[1])
        if fb_width == 0 or fb_height == 0:
            return

        self._program["ProjMtx"] = (
            2.0 / display_width, 0.0, 0.0, 0.0,
            0.0, 2.0 / -display_height, 0.0, 0.0,
            0.0, 0.0, -1.0, 0.0,
            -1.0, 1.0, 0.0, 1.0,
        )

        self._program["Portal"] = self.portal

        draw_data.scale_clip_rects(fb_scale)

        self._ctx.enable_only(self._ctx.BLEND)
        self._ctx.blend_func = self._ctx.BLEND_DEFAULT

        self._font_texture.use(0)

        for commands in draw_data.cmd_lists:
            # Write the vertex and index buffer data without copying it
            self._vbo.write(commands.vtx_buffer_data)
            self._ibo.write(commands.idx_buffer_data)

            idx_pos = 0
            for command in commands:
                # Use low level pyglet call here instead because we only have the texture name
                gl.glBindTexture(gl.GL_TEXTURE_2D, command.texture_id)
                # Set scissor box
                x, y, z, w = command.clip_rect
                gl.glScissor(int(x), int(fb_height - w), int(z - x), int(w - y))

                if command.user_callback:
                    command.user_callback(self, draw_data, commands, command, command.user_callback_data)
                else:
                    self._vao.render(self._program, mode=self._ctx.TRIANGLES, vertices=command.elem_count, first=idx_pos)
                idx_pos += command.elem_count

        # Just reset scissor back to default/viewport
        gl.glScissor(*self._ctx.viewport)

    def refresh_font_texture(self):
        width, height, pixels = self.io.fonts.get_tex_data_as_rgba32()
        # Old font texture will be GCed if exist
        self._font_texture = self._ctx.texture((width, height), components=4, data=pixels)
        # Need to convert ctype to python object.  Can't do it from the c++ side evidently ...
        #self.io.fonts.tex_id = self._font_texture.glo
        self.io.fonts.tex_id = self._font_texture.glo.value
        self.io.fonts.clear_tex_data()

    def _create_device_objects(self):
        self._program = self._ctx.program(
            vertex_shader=self.VERTEX_SHADER_SRC,
            fragment_shader=self.FRAGMENT_SHADER_SRC,
        )
        self._program["Texture"] = 0
        self._vbo = self._ctx.buffer(reserve=aimgui.VERTEX_SIZE * 65536)
        self._ibo = self._ctx.buffer(reserve=aimgui.INDEX_SIZE * 65536)
        # NOTE: aimgui.INDEX_SIZE is type size for the index buffer. We might need to support 8 and 16 bit
        # but right now we are assuming 32 bit
        self._vao = self._ctx.geometry(
            [
                BufferDescription(
                    self._vbo,
                    "2f 2f 4f1",
                    ("Position", "UV", "Color"),
                    normalized=("Color",)
                ),
            ],
            index_buffer = self._ibo,
        )           

    def _invalidate_device_objects(self):
        # NOTE: OpenGL resource will automatically be released
        self._font_texture = None
        self._vbo = None
        self._ibo = None
        self._vao = None
        self._program = None
        self.io.fonts.texture_id = 0

    def shutdown(self):
        self._invalidate_device_objects()


class ArcadeGuiBase:
    REVERSE_KEY_MAP = {
        key.TAB: aimgui.KEY_TAB,
        key.LEFT: aimgui.KEY_LEFT_ARROW,
        key.RIGHT: aimgui.KEY_RIGHT_ARROW,
        key.UP: aimgui.KEY_UP_ARROW,
        key.DOWN: aimgui.KEY_DOWN_ARROW,
        key.PAGEUP: aimgui.KEY_PAGE_UP,
        key.PAGEDOWN: aimgui.KEY_PAGE_DOWN,
        key.HOME: aimgui.KEY_HOME,
        key.END: aimgui.KEY_END,
        key.DELETE: aimgui.KEY_DELETE,
        key.SPACE: aimgui.KEY_SPACE,
        key.BACKSPACE: aimgui.KEY_BACKSPACE,
        key.RETURN: aimgui.KEY_ENTER,
        key.ESCAPE: aimgui.KEY_ESCAPE,
        key.A: aimgui.KEY_A,
        key.C: aimgui.KEY_C,
        key.V: aimgui.KEY_V,
        key.X: aimgui.KEY_X,
        key.Y: aimgui.KEY_Y,
        key.Z: aimgui.KEY_Z,
    }

    def _set_pixel_ratio(self, window):
        window_size = window.get_size()
        self.io.display_size = window_size
        # It is conceivable that the pyglet version will not be solely
        # determinant of whether we use the fixed or programmable, so do some
        # minor introspection here to check.
        if hasattr(window, 'get_viewport_size'):
            viewport_size = window.get_viewport_size()
            self.io.display_framebuffer_scale = compute_framebuffer_scale(window_size, viewport_size)
        elif hasattr(window, 'get_pixel_ratio'):
            self.io.display_framebuffer_scale = (window.get_pixel_ratio(),
                                        window.get_pixel_ratio())
        else:
            # Default to 1.0 in this unlikely circumstance
            self.io.display_framebuffer_scale = (1.0, 1.0)

    def _attach_callbacks(self, window):
        window.push_handlers(
            self.on_mouse_motion,
            self.on_key_press,
            self.on_key_release,
            self.on_text,
            self.on_mouse_drag,
            self.on_mouse_press,
            self.on_mouse_release,
            self.on_mouse_scroll,
            self.on_resize,
        )

    def _on_mods_change(self, mods):
        self.io.key_ctrl = mods & key.MOD_CTRL
        self.io.key_super = mods & key.MOD_COMMAND
        self.io.key_alt = mods & key.MOD_ALT
        self.io.key_shift = mods & key.MOD_SHIFT

    def on_mouse_motion(self, x, y, dx, dy):
        self.io.mouse_pos = x, self.io.display_size[1] - y

    def on_key_press(self, key_pressed, mods):
        if key_pressed in self.REVERSE_KEY_MAP:
            #self.io.keys_down[self.REVERSE_KEY_MAP[key_pressed]] = True
            self.io.set_key_down(self.REVERSE_KEY_MAP[key_pressed], True)
        self._on_mods_change(mods)

    def on_key_release(self, key_released, mods):
        if key_released in self.REVERSE_KEY_MAP:
            #self.io.keys_down[self.REVERSE_KEY_MAP[key_released]] = False
            self.io.set_key_down(self.REVERSE_KEY_MAP[key_released], False)
        self._on_mods_change(mods)

    def on_text(self, text):
        io = aimgui.get_io()

        for char in text:
            io.add_input_character(ord(char))

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.io.mouse_pos = x, self.io.display_size[1] - y
        
        if button == mouse.LEFT:
            self.io.set_mouse_down(0, True)

        if button == mouse.RIGHT:
            self.io.set_mouse_down(1, True)

        if button == mouse.MIDDLE:
            self.io.set_mouse_down(2, True)


    def on_mouse_press(self, x, y, button, modifiers):
        self.io.mouse_pos = x, self.io.display_size[1] - y
        code = 0
        if button == mouse.LEFT:
            code = 0
        elif button == mouse.RIGHT:
            code = 1
        elif button == mouse.MIDDLE:
            code = 2

        self.io.set_mouse_down(code, True)

    def on_mouse_release(self, x, y, button, modifiers):
        self.io.mouse_pos = x, self.io.display_size[1] - y
        code = 0; delay = .2
        if button == mouse.LEFT:
            delay = 0
        elif button == mouse.RIGHT:
            code = 1
        elif button == mouse.MIDDLE:
            code = 2
        # Need a slight delay for touch events
        clock.schedule_once(lambda delta_time : self.io.set_mouse_down(code, False), delay)


    def on_mouse_scroll(self, x, y, mods, scroll):
        self.io.mouse_wheel = scroll

    def on_resize(self, width, height):
        self.io.display_size = width, height


class ArcadeGui(ArcadeGuiBase):
    def __init__(self, window, attach_callbacks=True):
        self.window = window

        self.context = aimgui.create_context()
        aimgui.set_current_context(self.context)

        self.io = aimgui.get_io()

        self.renderer = ArcadeRenderer(window)
        '''
        window_size = window.get_size()
        viewport_size = window.get_viewport_size()

        self.io.display_size = window_size
        self.io.display_framebuffer_scale = compute_framebuffer_scale(window_size, viewport_size)
        '''
        self._set_pixel_ratio(window)

        if attach_callbacks:
            window.push_handlers(
                self.on_mouse_motion,
                self.on_key_press,
                self.on_key_release,
                self.on_text,
                self.on_mouse_drag,
                self.on_mouse_press,
                self.on_mouse_release,
                self.on_mouse_scroll,
                self.on_resize,
            )

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
