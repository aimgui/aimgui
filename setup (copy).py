import sys
import setuptools

class get_pybind_include(object):
    def __str__(self):
        import pybind11
        print('get_pybind_include', pybind11.get_include())
        return pybind11.get_include()

class get_pybind_user_include(object):
    def __str__(self):
        import pybind11
        print('get_pybind_user_include', pybind11.get_include(True))
        return pybind11.get_include(True)

if sys.platform == 'win32':
  compile_args = [
    '/bigobj',
    '/DImTextureID=int',
    '/DIMGUI_DISABLE_OBSOLETE_FUNCTIONS=1',
  ]
else:
  compile_args = [
    '-std=c++14',
    '-Wno-error',
    '-Wno-format-security',
    #'-Wno-null-conversion',
    '-DImTextureID=int',
    '-DIMGUI_DISABLE_OBSOLETE_FUNCTIONS=1',
  ]

module = setuptools.Extension("aimgui", [
    'extern/imgui/imgui.cpp',
    'extern/imgui/imgui_demo.cpp',
    'extern/imgui/imgui_draw.cpp',
    'extern/imgui/imgui_widgets.cpp',
    'src/aimgui/aimgui.cpp',
  ],
  include_dirs = [get_pybind_include(), get_pybind_user_include(), 'extern/imgui'],
  extra_compile_args = compile_args,
  language = 'c++',
)
print('module', module)

setuptools.setup(
  name             = 'aimgui',
  description      = 'Advanced ImGui',
  version          = '0.1.0',
  url              = 'http://github.com/kfields/aimgui',
  license          = 'MIT',
  author           = 'kfields',
  packages         = setuptools.find_packages(),
  #package_data={'aimgui': ['*.so']},
  ext_modules      = [module],
  setup_requires   = ['pybind11'],
)
