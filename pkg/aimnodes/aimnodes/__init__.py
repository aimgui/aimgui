__version__ = '0.1.0'

import aimgui

aimgui.add_plugin(__file__)

from libaimnodes import *

'''
__version__ = '0.1.0'

import sys
import platform
from pathlib import Path

version = platform.python_version_tuple()

LIB_PATH = Path(__file__).parent.parent / '_skbuild' / f"{platform.system().lower()}-{platform.machine()}-{version[0]}.{version[1]}" / "cmake-build"
#print('LIB_PATH:  ', LIB_PATH)

sys.path.insert(0, str(LIB_PATH))
#print('SYS_PATH:  ',sys.path)

#import libaimnodes as core 
from libaimnodes import *
'''