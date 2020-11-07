from typing import Counter
from pyo import *

import aimgui

class Drawable:
    def __init__(self):
        self.drawables = []

    def draw(self):
        for drawable in self.drawables:
            drawable.draw()

class PyoObjectControl(Drawable):
    counter = 0
    @classmethod
    def produce(self, obj, map_list=None, title=None):
        return kinds[obj.__class__.__name__](obj, map_list, title)

    def draw(self):
        width = 20
        height = 100

        aimgui.begin(self.title)
        for i, m in enumerate(self._map_list):
            key, init, mini, maxi, scl, res, dataOnly = m.name, m.init, m.min, m.max, m.scale, m.res, m.dataOnly
            # filters PyoObjects
            if type(init) not in [list, float, int]:
                continue
            value = getattr(self._obj, key)
            speed = maxi / 100
            if key == 'phase':
                #print(value)
                print('scl', scl)
                print('mini:  ', mini)
                print('maxi:  ', maxi)
                print('speed:  ', speed)
                #if speed > 1.:
                #    speed = 1.

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
                    setattr(self._obj, key, value)
            elif type(value) is float:
                changed, value = aimgui.drag_float(
                    key,
                    value,
                    speed,
                    v_min=mini, v_max=maxi,
                    format="%0.3f"
                )
                if changed:
                    setattr(self._obj, key, value)

        aimgui.end()

    def __init__(self, obj=None, map_list=None, title=None):
        self.values = []
        if not title:
            title = obj.__class__.__name__
        self.title = title + '##' + str(self.counter)
        self.counter += 1
        from pyo.lib.controls import SigTo
        '''
        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(9999, "Close\tCtrl+W", kind=wx.ITEM_NORMAL)
        self.fileMenu.Bind(wx.EVT_MENU, self._destroy, id=9999)
        self.fileMenu.AppendSeparator()
        self.fileMenu.Append(
            10000, "Copy all parameters to the clipboard (4 digits of precision)\tCtrl+C", kind=wx.ITEM_NORMAL
        )
        self.Bind(wx.EVT_MENU, self.copy, id=10000)
        self.fileMenu.Append(
            10001, "Copy all parameters to the clipboard (full precision)\tShift+Ctrl+C", kind=wx.ITEM_NORMAL
        )
        self.Bind(wx.EVT_MENU, self.copy, id=10001)
        self.menubar.Append(self.fileMenu, "&File")
        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_CLOSE, self._destroy)
        '''
        self._obj = obj
        self._map_list = map_list
        self._sliders = []
        self._excluded = []
        self._values = {}
        self._displays = {}
        self._maps = {}
        self._sigs = {}
        '''
        panel = wx.Panel(self)
        panel.SetBackgroundColour(BACKGROUND_COLOUR)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        self.box = wx.FlexGridSizer(10, 2, 5, 5)

        for i, m in enumerate(self._map_list):
            key, init, mini, maxi, scl, res, dataOnly = m.name, m.init, m.min, m.max, m.scale, m.res, m.dataOnly
            # filters PyoObjects
            if type(init) not in [list, float, int]:
                self._excluded.append(key)
            else:
                self._maps[key] = m
                # label (param name)
                if dataOnly:
                    label = wx.StaticText(panel, -1, key + " *")
                else:
                    label = wx.StaticText(panel, -1, key)
                # create and pack slider
                if type(init) != list:
                    if scl == "log":
                        scl = True
                    else:
                        scl = False
                    if res == "int":
                        res = True
                    else:
                        res = False
                    self._sliders.append(
                        ControlSlider(
                            panel,
                            mini,
                            maxi,
                            init,
                            log=scl,
                            size=(300, 16),
                            outFunction=Command(self.setval, key),
                            integer=res,
                            ctrllabel=key,
                        )
                    )
                    self.box.AddMany([(label, 0, wx.LEFT, 5), (self._sliders[-1], 1, wx.EXPAND | wx.LEFT, 5)])
                else:
                    self._sliders.append(MultiSlider(panel, init, key, self.setval, m, ctrllabel=key))
                    self.box.AddMany([(label, 0, wx.LEFT, 5), (self._sliders[-1], 1, wx.EXPAND | wx.LEFT, 5)])
                # set obj attribute to PyoObject SigTo
                if not dataOnly:
                    self._values[key] = init
                    self._sigs[key] = SigTo(init, 0.025, init)
                    refStream = self._obj.getBaseObjects()[0]._getStream()
                    server = self._obj.getBaseObjects()[0].getServer()
                    for k in range(len(self._sigs[key].getBaseObjects())):
                        curStream = self._sigs[key].getBaseObjects()[k]._getStream()
                        server.changeStreamPosition(refStream, curStream)
                    setattr(self._obj, key, self._sigs[key])
        self.box.AddGrowableCol(1, 1)
        mainBox.Add(self.box, 1, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 10)

        panel.SetSizerAndFit(mainBox)
        self.SetClientSize(panel.GetSize())
        self.SetMinSize(self.GetSize())
        self.SetMaxSize((-1, self.GetSize()[1]))
        '''
    def _destroy(self, event):
        for m in self._map_list:
            key = m.name
            if key not in self._excluded and key in self._values:
                setattr(self._obj, key, self._values[key])
                del self._sigs[key]
        self.Destroy()

    def setval(self, key, x):
        if key in self._values:
            self._values[key] = x
            setattr(self._sigs[key], "value", x)
        else:
            setattr(self._obj, key, x)

    def copy(self, evt):
        labels = [slider.getCtrlLabel() for slider in self._sliders]
        values = [slider.GetValue() for slider in self._sliders]
        if evt.GetId() == 10000:
            pstr = ""
            for i in range(len(labels)):
                pstr += "%s=" % labels[i]
                if type(values[i]) == list:
                    pstr += "["
                    pstr += ", ".join(["%.4f" % val for val in values[i]])
                    pstr += "]"
                else:
                    pstr += "%.4f" % values[i]
                if i < (len(labels) - 1):
                    pstr += ", "
        else:
            pstr = ""
            for i in range(len(labels)):
                pstr += "%s=" % labels[i]
                if type(values[i]) == list:
                    pstr += "["
                    pstr += ", ".join([str(val) for val in values[i]])
                    pstr += "]"
                else:
                    pstr += str(values[i])
                if i < (len(labels) - 1):
                    pstr += ", "
        data = wx.TextDataObject(pstr)
        if wx.TheClipboard.Open():
            wx.TheClipboard.Clear()
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()

class FMControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        super().__init__(obj, map_list, title)
        print('init')
        self._map_list = [
            SLMap(10, 500, "lin", "carrier", obj._carrier),
            SLMap(0.01, 10, "lin", "ratio", obj._ratio),
            SLMap(0, 20, "lin", "index", obj._index),
            SLMapMul(obj._mul),
        ]
        #PyoObject.ctrl(self, map_list, title)

class SineControl(PyoObjectControl):
    def __init__(self, obj, map_list=None, title=None):
        super().__init__(obj, map_list, title)
        print('init')
        self._map_list = [SLMapFreq(obj._freq), SLMapPhase(obj._phase), SLMapMul(obj._mul)]
        #PyoObject.ctrl(self, map_list, title)

kinds = {
    "FM": FMControl,
    "Sine": SineControl
}