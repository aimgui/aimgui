import os
from ctypes import Structure, c_float, c_uint32, sizeof, c_bool, c_int
from pathlib import Path

from loguru import logger
import numpy as np
import openmesh as om

import aimgfx
from aimgfx.utils import as_void_ptr
from aimgfx.utils.shaders_utils import ShaderType, load_shader
from aimgfx.constants import *

from aimgfx.window import Window
from aimgfx.utils.matrix_utils import look_at, proj, rotate_xy

logger.enable("bunnies")



bunny_path = Path(__file__).parent.parent / "assets" / "meshes" / "bunny.obj"
bunny_mesh = om.read_trimesh(str(bunny_path))

num_vertices = bunny_mesh.n_vertices()
bunny_vertices = bunny_mesh.points()

aimgfx_states = (
    0,
    BGFX_STATE_PT_TRISTRIP,
    BGFX_STATE_PT_LINES,
    BGFX_STATE_PT_LINESTRIP,
    BGFX_STATE_PT_POINTS,
)

root_path = Path(__file__).parent.parent / "assets" / "shaders"

class Bunnies(Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.elapsed_time = 0
        self.write_r = c_bool(True)
        self.write_g = c_bool(True)
        self.write_b = c_bool(True)
        self.write_a = c_bool(True)
        self.primitive_geometry = c_int(0)

        self.init_conf = aimgfx.Init()
        self.init_conf.debug = True
        self.init_conf.resolution.width = self.width
        self.init_conf.resolution.height = self.height
        self.init_conf.resolution.reset = BGFX_RESET_VSYNC

        self.bunny_mesh = bunny_mesh

    def init(self, platform_data):
        aimgfx.set_platform_data(platform_data)
        aimgfx.render_frame()
        aimgfx.init(self.init_conf)
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format,
        )

        aimgfx.set_debug(BGFX_DEBUG_TEXT)
        aimgfx.set_view_clear(0, BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH, 0x443355FF, 1.0, 0)

        # Create time uniform
        self.time_uniform = aimgfx.create_uniform("u_time", aimgfx.UniformType.VEC4)

        self.vertex_layout = aimgfx.VertexLayout()
        #self.vertex_layout.begin().add(aimgfx.Attrib.POSITION, 3, aimgfx.AttribType.FLOAT).add(aimgfx.Attrib.COLOR0, 4, aimgfx.AttribType.UINT8, True).end()
        self.vertex_layout.begin().add(aimgfx.Attrib.POSITION, 3, aimgfx.AttribType.FLOAT).end()
        # Create static vertex buffer
        vb_memory = aimgfx.copy(as_void_ptr(bunny_vertices), num_vertices)
        
        self.vertex_buffer = aimgfx.create_vertex_buffer(vb_memory, self.vertex_layout)

        self.index_buffers = []

        ib_memory = aimgfx.copy(as_void_ptr(bunny_mesh.face_vertex_indices()), bunny_mesh.n_faces())
        self.index_buffer = aimgfx.create_index_buffer(ib_memory)
        #ib_memory = aimgfx.copy(as_void_ptr(primitives[i]), primitives[i].nbytes)
        #self.index_buffers.append(aimgfx.create_index_buffer(ib_memory))

        # Create program from shaders.
        self.main_program = aimgfx.create_program(
            load_shader(
                "mesh.VertexShader.vert", ShaderType.VERTEX, root_path=root_path
            ),
            load_shader(
                "mesh.FragmentShader.frag", ShaderType.FRAGMENT, root_path=root_path
            ),
            True,
        )

    def shutdown(self):
        for index_buffer in self.index_buffers:
            aimgfx.destroy(index_buffer)
        aimgfx.destroy(self.vertex_buffer)
        aimgfx.destroy(self.main_program)
        aimgfx.shutdown()

    def update(self, dt):
        self.elapsed_time += dt
        mouse_x, mouse_y, buttons_states = self.get_mouse_state()

        at = (c_float * 3)(*[0.0, 1.0, 0.0])
        eye = (c_float * 3)(*[0.0, 1.0, -2.5])
        up = (c_float * 3)(*[0.0, 1.0, 0.0])

        view = look_at(eye, at, up)
        projection = proj(60.0, self.width / self.height, 0.1, 100.0)

        #aimgfx.set_view_transform(0, as_void_ptr(view), as_void_ptr(projection))
        aimgfx.set_view_rect(0, 0, 0, self.width, self.height)

        aimgfx.touch(0)

        mtx = rotate_xy(0, self.elapsed_time * 0.37)

        aimgfx.set_uniform(
            self.time_uniform,
            as_void_ptr((c_float * 4)(self.elapsed_time, 0.0, 0.0, 0.0)),
        )

        # Set vertex and index buffer.
        aimgfx.set_vertex_buffer(0, self.vertex_buffer, 0, num_vertices)
        aimgfx.set_index_buffer(self.index_buffer)

        aimgfx.submit(0, self.main_program, 0)
        #self.mesh.submit(0, self.main_program, mtx)

        aimgfx.frame()

    def resize(self, width, height):
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format
        )

def main():
    bunnies = Bunnies(1280, 720, "examples/bunnies")
    bunnies.run()

if __name__ == "__main__":
    main()