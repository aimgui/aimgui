import sys, os
import setuptools
from skbuild import setup

from aimplot_setup.install import install
from aimplot_setup.develop import develop

setup(
    name             = 'aimplot',
    description      = 'Advanced ImPlot',
    version          = '0.1.0',
    url              = 'http://github.com/aimgui/aimgui',
    license          = 'MIT',
    author           = 'kfields',
    packages         = setuptools.find_packages(exclude=["__aimgen__"]),
    cmdclass = {
        'install': install,
        'develop': develop
    },
)
