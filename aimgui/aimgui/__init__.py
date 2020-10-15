__version__ = '0.1.0'

import sys
import platform
from pathlib import Path

version = platform.python_version_tuple()

LIB_PATH = Path(__file__).parent.parent / '_skbuild' / f"{platform.system().lower()}-{platform.machine()}-{version[0]}.{version[1]}" / "cmake-build"
print('LIB_PATH:  ', LIB_PATH)

sys.path.insert(0, str(LIB_PATH))
print(sys.path)

import libaimgui as core 
from libaimgui import *

from aimgui.extra import *

VERTEX_BUFFER_POS_OFFSET = core.get_vertex_buffer_vertex_pos_offset()
VERTEX_BUFFER_UV_OFFSET = core.get_vertex_buffer_vertex_uv_offset()
VERTEX_BUFFER_COL_OFFSET = core.get_vertex_buffer_vertex_col_offset()

VERTEX_SIZE = core.get_vertex_buffer_vertex_size()
INDEX_SIZE = core.get_index_buffer_index_size()
