from aimgui.impl.arcade import ArcadeGui
import aimplot
from .widgets import PyoObjectControl, PyoObjectView, PyoScope, PyoSpectrum

class PyoGui(ArcadeGui):
    def __init__(self, window, attach_callbacks=True):
        super().__init__(window, attach_callbacks)
        aimplot.create_context()
        self.drawables = []

    def clear(self):
        self.drawables = []

    def draw(self):
        for drawable in self.drawables:
            drawable.draw()

    def ctrl(self, obj, map_list=None, title=None):
        ctrl = PyoObjectControl.produce(obj, map_list, title)
        self.drawables.append(ctrl)
        return ctrl

    def view(self, obj, title=None):
        ctrl = PyoObjectView.produce(obj, title)
        self.drawables.append(ctrl)
        return ctrl

    # def __init__(self, input, length=0.05, gain=0.67, function=None, wintitle="Scope"):
    def scope(self, input, wintitle="Scope"):
        sc = PyoScope(input, wintitle=wintitle)
        self.drawables.append(sc)
        return sc

    #def __init__(self, input, size=1024, wintype=2, function=None, wintitle="Spectrum"):
    def spectrum(self, input):
        sc = PyoSpectrum(input)
        self.drawables.append(sc)
        return sc