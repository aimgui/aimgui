from ctypes import c_float
from pathlib import Path

from loguru import logger

import aimgfx
from aimgfx.utils import as_void_ptr
#from aimgfx.utils.mesh_utils import Mesh
from aimgfx.utils.shaders_utils import ShaderType, load_shader
from aimgfx.constants import *
from aimgfx.window import Window
from aimgfx.utils.matrix_utils import look_at, proj, rotate_xy

logger.enable("aimgfx")

root_path = Path(__file__).parent.parent / "assets" / "shaders"
###
import openmesh as om
from typing import List

class Mesh:
    def __init__(self, file_path: Path, ram_copy=False):
        logger.debug(f"Loading mesh (RAM {ram_copy}): {file_path}")
        str_file_path = str(file_path)
        self.om_mesh = om.read_trimesh(str_file_path)

    def submit(
        self,
        view_id: int,
        program: aimgfx.ProgramHandle,
        matrix: List[float],
        state=BGFX_STATE_MASK,
    ):
        self.internal_mesh.submit(view_id, program, matrix, state)

    def destroy(self):
        self.internal_mesh.unload()
###

class MeshExample(Window):
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

        # Create time uniform
        self.time_uniform = aimgfx.create_uniform("u_time", aimgfx.UniformType.VEC4)

        # Load Bunny mesh
        self.mesh = Mesh(
            (
                Path(__file__).parent.parent / "assets" / "meshes" / "bunny.obj"
            ).absolute()
        )

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
        self.mesh.destroy()
        aimgfx.destroy(self.main_program)
        aimgfx.destroy(self.time_uniform)
        aimgfx.shutdown()

    def update(self, dt):
        self.elapsed_time += dt
        mouse_x, mouse_y, buttons_states = self.get_mouse_state()

        at = (c_float * 3)(*[0.0, 1.0, 0.0])
        eye = (c_float * 3)(*[0.0, 1.0, -2.5])
        up = (c_float * 3)(*[0.0, 1.0, 0.0])

        view = look_at(eye, at, up)
        projection = proj(60.0, self.width / self.height, 0.1, 100.0)

        aimgfx.set_view_transform(0, as_void_ptr(view), as_void_ptr(projection))
        aimgfx.set_view_rect(0, 0, 0, self.width, self.height)

        aimgfx.touch(0)

        mtx = rotate_xy(0, self.elapsed_time * 0.37)

        aimgfx.set_uniform(
            self.time_uniform,
            as_void_ptr((c_float * 4)(self.elapsed_time, 0.0, 0.0, 0.0)),
        )

        self.mesh.submit(0, self.main_program, mtx)

        aimgfx.frame()

    def resize(self, width, height):
        aimgfx.reset(
            self.width, self.height, BGFX_RESET_VSYNC, self.init_conf.resolution.format
        )

def main():
    textures = MeshExample(1280, 720, "examples/mesh")
    textures.run()

if __name__ == "__main__":
    main()