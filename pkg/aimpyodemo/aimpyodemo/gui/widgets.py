import string

from pyo import *

import aimgui
import aimplot

class Drawable:
    def __init__(self):
        self.drawables = []

    def draw(self):
        for drawable in self.drawables:
            drawable.draw()

class PyoScope(Drawable):
    def __init__(self, input, length=0.05, gain=0.67, function=None, wintitle="Scope"):
        self.title = wintitle
        self.data = []
        def fn(data):
            self.data = data

        self.scope = Scope(input, function=fn)

    def draw(self):
        letters = list(string.ascii_uppercase)
        aimgui.begin(self.title)
        aimplot.set_next_plot_limits(0,500,0,500)
        if aimplot.begin_plot("Scope Plot"):
            for data in self.data:
                #print(data)
                _, data = zip(*data)
                aimplot.plot_line(letters.pop(), data, len(data))
            aimplot.end_plot()
        aimgui.end()

class PyoSpectrum(Drawable):
    def __init__(self, input, size=1024, wintype=2, function=None, wintitle="Spectrum"):
        self.data = []
        def fn(data):
            self.data = data

        self.scope = Spectrum(input, function=fn)

    def draw(self):
        letters = list(string.ascii_uppercase)
        aimgui.begin("Spectrum")
        aimplot.set_next_plot_limits(0,500,0,500)
        if aimplot.begin_plot("Spectrum Plot"):
            for data in self.data:
                #print(data)
                _, data = zip(*data)
                aimplot.plot_line(letters.pop(), data, len(data))
            aimplot.end_plot()
        aimgui.end()

class PyoObjectControl(Drawable):
    counter = 0
    @classmethod
    def produce(self, obj, map_list=None, title=None):
        return controls[obj.__class__.__name__](obj, map_list, title)

    def __init__(self, obj=None, map_list=None, title=None):
        self.values = []
        if not title:
            title = obj.__class__.__name__
        self.title = title + '##' + str(self.counter)
        self.counter += 1

        self._obj = obj
        self._map_list = map_list
        self._sliders = []
        self._excluded = []
        self._values = {}
        self._displays = {}
        self._maps = {}
        self._sigs = {}

    def draw_multislider(self, m, arr):
        key, init, mini, maxi, scl, res, dataOnly = m.name, m.init, m.min, m.max, m.scale, m.res, m.dataOnly
        speed = maxi / 100
        arr_changed = False
        for i in range(0, len(arr)):
            value = arr[i]
            aimgui.push_id(i)
            if type(value) is int:
                changed, value = aimgui.drag_int(
                    key,
                    value,
                    speed,
                    v_min=int(mini),
                    v_max=int(maxi),
                    #format="%0.3f"
                )
                if changed:
                    arr[i] = value
                    arr_changed |= True
            elif type(value) is float:
                changed, value = aimgui.drag_float(
                    key,
                    value,
                    speed,
                    v_min=mini, v_max=maxi,
                    format="%0.3f"
                )
                if changed:
                    arr[i] = value
                    arr_changed |= True
            aimgui.pop_id()
        return arr_changed

    def draw_slider(self, m):
            key, init, mini, maxi, scl, res, dataOnly = m.name, m.init, m.min, m.max, m.scale, m.res, m.dataOnly
            # filters PyoObjects
            if type(init) not in [list, float, int]:
                return
            changed = False
            value = getattr(self._obj, key)
            speed = maxi / 100
            '''
            if key == 'phase':
                #print(value)
                print('scl', scl)
                print('mini:  ', mini)
                print('maxi:  ', maxi)
                print('speed:  ', speed)
                #if speed > 1.:
                #    speed = 1.
            '''
            if type(value) is int:
                changed, value = aimgui.drag_int(
                    key,
                    value,
                    speed,
                    v_min=int(mini),
                    v_max=int(maxi),
                    #format="%0.3f"
                )
            elif type(value) is float:
                changed, value = aimgui.drag_float(
                    key,
                    value,
                    speed,
                    v_min=mini, v_max=maxi,
                    format="%0.3f"
                )
            elif type(value) is list:
                changed = self.draw_multislider(m, value)

            if changed:
                setattr(self._obj, key, value)

    def draw(self):
        aimgui.begin(self.title)

        for i, m in enumerate(self._map_list):
            self.draw_slider(m)

        aimgui.end()


class FMControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        super().__init__(obj, map_list, title)
        self._map_list = [
            SLMap(10, 500, "lin", "carrier", obj._carrier),
            SLMap(0.01, 10, "lin", "ratio", obj._ratio),
            SLMap(0, 20, "lin", "index", obj._index),
            SLMapMul(obj._mul),
        ]

class SineControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMapFreq(obj._freq), SLMapPhase(obj._phase), SLMapMul(obj._mul)]
        super().__init__(obj, map_list, title)

class SigControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMap(0, 1, "lin", "value", obj._value)]
        super().__init__(obj, map_list, title)

class InterpControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMap(0.0, 1.0, "lin", "interp", obj._interp), SLMapMul(obj._mul)]
        super().__init__(obj, map_list, title)
        
class SelectorControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMap(0, len(obj._inputs) - 1, "lin", "voice", obj._voice), SLMapMul(obj._mul)]
        super().__init__(obj, map_list, title)

class LFOControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [
                SLMap(0.1, obj.getSamplingRate() * 0.25, "log", "freq", obj._freq),
                SLMap(0.0, 1.0, "lin", "sharp", obj._sharp),
                SLMap(0, 7, "lin", "type", obj._type, "int", dataOnly=True),
                SLMapMul(obj._mul),
            ]
        super().__init__(obj, map_list, title)

class CrossFMControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [
                SLMap(10, 500, "lin", "carrier", obj._carrier),
                SLMap(0.01, 10, "lin", "ratio", obj._ratio),
                SLMap(0, 20, "lin", "ind1", obj._ind1),
                SLMap(0, 20, "lin", "ind2", obj._ind2),
                SLMapMul(obj._mul),
            ]
        super().__init__(obj, map_list, title)

class SigToControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMap(0, 10, "lin", "time", obj._time)]
        super().__init__(obj, map_list, title)

class PortControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [
                SLMap(0.001, 10.0, "log", "risetime", obj._risetime),
                SLMap(0.001, 10.0, "log", "falltime", obj._falltime),
            ]
        super().__init__(obj, map_list, title)

class LooperControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [
                SLMap(0.1, 2.0, "lin", "pitch", obj._pitch),
                SLMap(0.0, obj._table.getDur(), "lin", "start", obj._start),
                SLMap(0.01, obj._table.getDur(), "lin", "dur", obj._dur),
                SLMap(1, 50, "lin", "xfade", obj._xfade),
                SLMap(0, 3, "lin", "mode", obj._mode, res="int", dataOnly=True),
                SLMap(0, 2, "lin", "xfadeshape", obj._xfadeshape, res="int", dataOnly=True),
                SLMap(1, 4, "lin", "interp", obj._interp, res="int", dataOnly=True),
                SLMapMul(obj._mul),
            ]
        super().__init__(obj, map_list, title)

class NoiseControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        if not map_list:
            map_list = [SLMapMul(obj._mul)]
        super().__init__(obj, map_list, title)

class Particle2Control(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        tablesize = obj._table.getSize(False)
        if not map_list:
            map_list = [
                SLMap(1, 250, "lin", "dens", obj._dens),
                SLMap(0.25, 2.0, "lin", "pitch", obj._pitch),
                SLMap(0, tablesize, "lin", "pos", obj._pos, res="int"),
                SLMap(0.001, 1.0, "lin", "dur", obj._dur),
                SLMap(0.0, 1.0, "lin", "dev", obj._dev),
                SLMap(0.0, 1.0, "lin", "pan", obj._pan),
                SLMap(50.0, 18000.0, "log", "filterfreq", obj._filterfreq),
                SLMap(0.25, 100.0, "log", "filterq", obj._filterq),
                SLMap(0, 4.0, "lin", "filtertype", obj._filtertype, res="int"),
                SLMapMul(obj._mul),
            ]
        super().__init__(obj, map_list, title)

controls = {
    "FM": FMControl,
    "Sine": SineControl,
    "Sig": SigControl,
    "Interp": InterpControl,
    "Selector": SelectorControl,
    "LFO": LFOControl,
    "CrossFM": CrossFMControl,
    "SigTo": SigToControl,
    "Port": PortControl,
    "Looper": LooperControl,
    "Noise": NoiseControl,
    "Particle2": Particle2Control
}

class PyoObjectView(Drawable):
    counter = 0
    @classmethod
    def produce(self, obj, title=None):
        return views[obj.__class__.__name__](obj, title)

    def __init__(self, obj, title="Table waveform"):
        self.obj = obj
        if not title:
            title = obj.__class__.__name__
        self.title = title + '##' + str(self.counter)
        self.counter += 1

class TableView(PyoObjectView):
    def __init__(self, obj, title="Table waveform"):
        super().__init__(obj, title)

    def draw(self):
        samples = self.obj._base_objs[0].getViewTable((500, 200))
        _, samples = zip(*samples)
        letters = list(string.ascii_uppercase)
        aimgui.begin(self.title)
        aimplot.set_next_plot_limits(0,500,0,200)
        if aimplot.begin_plot("Table View"):
            aimplot.plot_line(letters.pop(), samples, len(samples))
            aimplot.end_plot()
        aimgui.end()


views = {
    "ExpTable": TableView,
    "SndTable": TableView,
    "WinTable": TableView,
    "LinTable": TableView,
    "AtanTable": TableView,
}

class PyoObjectGraph(Drawable):
    counter = 0
    @classmethod
    def produce(self, obj, yrange=(0.0, 1.0), title=None):
        return graphs[obj.__class__.__name__](obj, yrange, title)

    def __init__(self, obj, yrange, title="Table waveform"):
        self.obj = obj
        self.pts = obj.getPoints()
        self.xrange = obj._size
        self.yrange = yrange
        self.title = title

class TableGraph(PyoObjectGraph):
    def __init__(self, obj, yrange=(0.0, 1.0), title="Table waveform"):
        super().__init__(obj, yrange, title)

    def draw(self):
        letters = list(string.ascii_uppercase)
        aimgui.begin(self.title)
        aimplot.set_next_plot_limits(0, self.xrange, self.yrange[0], self.yrange[1])
        if aimplot.begin_plot("Table Waveform"):
            xs, ys = zip(*self.pts)
            aimplot.plot_line(letters.pop(), xs, ys, len(self.pts))
            aimplot.end_plot()
        aimgui.end()


graphs = {
    "CosTable": TableGraph,
    "ExpTable": TableGraph,
    "LinTable": TableGraph,
}
