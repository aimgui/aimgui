import os
from ctypes import Structure, c_float, c_uint32, sizeof
from pathlib import Path

import numpy as np
from PIL import Image
from loguru import logger

import aimgfx
from aimgfx.utils import as_void_ptr
from aimgfx.utils.shaders_utils import ShaderType, load_shader
from aimgfx.constants import (
    BGFX_CLEAR_COLOR,
    BGFX_CLEAR_DEPTH,
    BGFX_DEBUG_TEXT,
    BGFX_RESET_VSYNC,
    BGFX_STATE_WRITE_A,
    BGFX_STATE_WRITE_Z,
    BGFX_STATE_DEPTH_TEST_LESS,
    BGFX_STATE_MSAA,
    BGFX_TEXTURE_RT,
    BGFX_STATE_WRITE_RGB,
)
from aimgfx.window import Window
from aimgfx.utils.matrix_utils import look_at, proj, rotate_xy

logger.enable("aimgfx")


class PosColorTexVertex(Structure):
    _fields_ = [
        ("m_x", c_float),
        ("m_y", c_float),
        ("m_z", c_float),
        ("m_abgr", c_uint32),
        ("m_tex_u", c_float),
        ("m_tex_v", c_float),
    ]


num_vertices = 24

cube_vertices = (PosColorTexVertex * 24)(
    PosColorTexVertex(-1.0, 1.0, 1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(1.0, 1.0, 1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(-1.0, -1.0, 1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(1.0, -1.0, 1.0, 0xFF000000, 1, 1),
    PosColorTexVertex(-1.0, 1.0, -1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(1.0, 1.0, -1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(-1.0, -1.0, -1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(1.0, -1.0, -1.0, 0xFF000000, 1, 1),
    PosColorTexVertex(-1.0, 1.0, 1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(1.0, 1.0, 1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(-1.0, 1.0, -1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(1.0, 1.0, -1.0, 0xFF000000, 1, 1),
    PosColorTexVertex(-1.0, -1.0, 1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(1.0, -1.0, 1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(-1.0, -1.0, -1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(1.0, -1.0, -1.0, 0xFF000000, 1, 1),
    PosColorTexVertex(1.0, -1.0, 1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(1.0, 1.0, 1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(1.0, -1.0, -1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(1.0, 1.0, -1.0, 0xFF000000, 1, 1),
    PosColorTexVertex(-1.0, -1.0, 1.0, 0xFF000000, 0, 0),
    PosColorTexVertex(-1.0, 1.0, 1.0, 0xFF000000, 1, 0),
    PosColorTexVertex(-1.0, -1.0, -1.0, 0xFF000000, 0, 1),
    PosColorTexVertex(-1.0, 1.0, -1.0, 0xFF000000, 1, 1),
)

cube_indices = np.array(
    [
        0,
        2,
        1,
        1,
        2,
        3,
        4,
        5,
        6,
        5,
        7,
        6,
        8,
        10,
        9,
        9,
        10,
        11,
        12,
        13,
        14,
        13,
        15,
        14,
        16,
        18,
        17,
        17,
        18,
        19,
        20,
        21,
        22,
        21,
        23,
        22,
    ],
    dtype=np.uint16,
)

root_path = Path(__file__).parent.parent / "assets" / "shaders"


class Textures(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.elapsed_time = 0

        self.init_conf = aimgfx.Init()
        self.init_conf.debug = True
        self.init_conf.resolution.width = self.width
        self.init_conf.resolution.height = self.height
        self.init_conf.resolution.reset = BGFX_RESET_VSYNC

    def init(self, platform_data):
        aimgfx.set_platform_data(platform_data)
        aimgfx.render_frame()
        aimgfx.init(self.init_conf)
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format,
        )

        aimgfx.set_debug(BGFX_DEBUG_TEXT)
        aimgfx.set_view_clear(0, BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH, 0x443355FF, 1.0, 0)

        self.vertex_layout = aimgfx.VertexLayout()
        self.vertex_layout.begin().add(
            aimgfx.Attrib.POSITION, 3, aimgfx.AttribType.FLOAT
        ).add(aimgfx.Attrib.COLOR0, 4, aimgfx.AttribType.UINT8, True).add(
            aimgfx.Attrib.TEX_COORD0, 2, aimgfx.AttribType.FLOAT
        ).end()

        # Create static vertex buffer
        vb_memory = aimgfx.copy(
            as_void_ptr(cube_vertices), sizeof(PosColorTexVertex) * num_vertices
        )
        self.vertex_buffer = aimgfx.create_vertex_buffer(vb_memory, self.vertex_layout)

        # Create index buffer
        ib_memory = aimgfx.copy(as_void_ptr(cube_indices), cube_indices.nbytes)
        self.index_buffer = aimgfx.create_index_buffer(ib_memory)

        # Create texture uniform
        self.texture_uniform = aimgfx.create_uniform("s_tex", aimgfx.UniformType.SAMPLER)

        # Load the image using PIL and make the texture
        logo = Image.open(
            Path(__file__).parent.parent / "assets" / "textures" / "python_logo.png"
        )
        image_bytes = logo.tobytes()
        logo_memory = aimgfx.copy(as_void_ptr(image_bytes), len(image_bytes))
        self.logo_texture = aimgfx.create_texture2_d(
            logo.width,
            logo.height,
            False,
            1,
            aimgfx.TextureFormat.RGBA8,
            BGFX_TEXTURE_RT,
            logo_memory,
        )

        # Create program from shaders.
        self.main_program = aimgfx.create_program(
            load_shader(
                "textures.VertexShader.vert", ShaderType.VERTEX, root_path=root_path
            ),
            load_shader(
                "textures.FragmentShader.frag", ShaderType.FRAGMENT, root_path=root_path
            ),
            True,
        )

    def shutdown(self):
        aimgfx.destroy(self.index_buffer)
        aimgfx.destroy(self.vertex_buffer)
        aimgfx.destroy(self.texture_uniform)
        aimgfx.destroy(self.logo_texture)
        aimgfx.destroy(self.main_program)
        aimgfx.shutdown()

    def update(self, dt):
        self.elapsed_time += dt
        mouse_x, mouse_y, buttons_states = self.get_mouse_state()

        at = (c_float * 3)(*[0.0, 0.0, 0.0])
        eye = (c_float * 3)(*[0.0, 0.0, -15.0])
        up = (c_float * 3)(*[0.0, 1.0, 0.0])

        view = look_at(eye, at, up)
        projection = proj(60.0, self.width / self.height, 0.1, 100.0)

        aimgfx.set_view_transform(0, as_void_ptr(view), as_void_ptr(projection))
        aimgfx.set_view_rect(0, 0, 0, self.width, self.height)

        aimgfx.touch(0)

        # Set the texture
        aimgfx.set_texture(0, self.texture_uniform, self.logo_texture)

        for yy in range(-2, 2):
            for xx in range(-2, 2):
                mtx = rotate_xy(
                    self.elapsed_time + xx * 0.51, self.elapsed_time + yy * 0.27
                )
                mtx[3, 0] = 4 + xx * 3.5
                mtx[3, 1] = 2 + yy * 3.5
                mtx[3, 2] = 0
                aimgfx.set_transform(as_void_ptr(mtx), 1)

                # Set vertex and index buffer.
                aimgfx.set_vertex_buffer(0, self.vertex_buffer, 0, num_vertices)
                aimgfx.set_index_buffer(self.index_buffer, 0, cube_indices.size)

                aimgfx.set_state(
                    0
                    | BGFX_STATE_WRITE_RGB
                    | BGFX_STATE_WRITE_A
                    | BGFX_STATE_WRITE_Z
                    | BGFX_STATE_DEPTH_TEST_LESS
                    | BGFX_STATE_MSAA,
                    0,
                )

                aimgfx.submit(0, self.main_program, 0, False)

        aimgfx.frame()

    def resize(self, width, height):
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format
        )

def main():
    textures = Textures(1280, 720, "examples/textures")
    textures.run()

if __name__ == "__main__":
    main()