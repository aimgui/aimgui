from array import array
from typing import List

from loguru import logger
from pathlib import Path


import openmesh as om

import aimgfx
from aimgfx.constants import BGFX_STATE_MASK


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
