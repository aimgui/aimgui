import sys
import setuptools
from skbuild import setup

from aimgui_setup.install import install
from aimgui_setup.develop import develop

setup(
    name             = 'aimgui',
    description      = 'Advanced ImGui',
    version          = '0.1.0',
    url              = 'http://github.com/kfields/aimgui',
    license          = 'MIT',
    author           = 'kfields',
    packages         = setuptools.find_packages(),
    #package_data={'aimgui': ['*.so']},
    #ext_modules      = [module],
    setup_requires   = ['pybind11', "setuptools", "wheel", "scikit-build", "cmake", "ninja"],
    cmdclass = {
        'install': install,
        'develop': develop
    },
)
