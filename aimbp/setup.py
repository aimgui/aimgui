import sys
import setuptools
from skbuild import setup

from aimbp_setup.install import install
from aimbp_setup.develop import develop

#INSTALL_REQUIRES = [ 'pybind11', "setuptools", "wheel", "scikit-build", "cmake", "ninja"]

setup(
    name             = 'aimbp',
    description      = 'Advanced ImBluePrints',
    version          = '0.1.0',
    url              = 'http://github.com/aimgui/aimgui',
    license          = 'MIT',
    author           = 'kfields',
    packages         = setuptools.find_packages(exclude=["__aimgen__"]),
    #package_data={'aimgui': ['*.so']},
    #ext_modules      = [module],
    #setup_requires   = ['pybind11', "wheel", "scikit-build", "cmake", "ninja"],
    #install_requires=INSTALL_REQUIRES,
    cmdclass = {
        'install': install,
        'develop': develop
    },
)
