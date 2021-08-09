#TODO: placeholder for future use

from setuptools.command.install import install as _install

class install(_install):
    def run(self):
        _install.run(self)
        print('aimgui:setup:install')
    