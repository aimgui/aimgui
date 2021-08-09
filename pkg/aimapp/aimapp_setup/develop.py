#TODO: placeholder for future use

from setuptools.command.develop import develop as _develop

class develop(_develop):
    def run(self):
        _develop.run(self)
        print('aimgui:setup:develop')
    