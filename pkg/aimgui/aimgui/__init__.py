__version__ = '0.1.0'

import sys
import platform
from pathlib import Path

def add_plugin(location):
  '''
  version = platform.python_version_tuple()
  os = platform.system().lower()
  build_dir = "cmake-build"
  if os == 'windows':
    os = 'win'
    build_dir = "cmake-build/Debug"

  LIB_PATH = Path(location).parent.parent / '_skbuild' / f"{os}-{platform.machine()}-{version[0]}.{version[1]}" / build_dir
  #print('LIB_PATH:  ', LIB_PATH)

  sys.path.insert(0, str(LIB_PATH))
  #print('SYS_PATH:  ',sys.path)
  '''
  LIB_PATH = Path(location).parent
  sys.path.insert(0, LIB_PATH)

add_plugin(__file__)

from . import _aimgui as core 
from ._aimgui import *

from aimgui.extra import *

#TODO:Belongs on the c++ side?

VERTEX_BUFFER_POS_OFFSET = core.get_vertex_buffer_vertex_pos_offset()
VERTEX_BUFFER_UV_OFFSET = core.get_vertex_buffer_vertex_uv_offset()
VERTEX_BUFFER_COL_OFFSET = core.get_vertex_buffer_vertex_col_offset()

VERTEX_SIZE = core.get_vertex_buffer_vertex_size()
INDEX_SIZE = core.get_index_buffer_index_size()

def rel(x, y):
    pos = core.get_cursor_screen_pos()
    x1 = pos[0] + x
    y1 = pos[1] + y
    return x1, y1
