from aimgui.impl.arcade import ArcadeGui

from .widgets import PyoObjectControl

class PyoGui(ArcadeGui):
    def __init__(self, window, attach_callbacks=True):
        super().__init__(window, attach_callbacks)
        self.drawables = []

    def clear(self):
        self.drawables = []

    def draw(self):
        for drawable in self.drawables:
            drawable.draw()

    def ctrl(self, obj, map_list=None, title=None):
        """
        Opens a sliders window to control the parameters of the object.
        Only parameters that can be set to a PyoObject are allowed
        to be mapped on a slider.

        If a list of values are given to a parameter, a multisliders
        will be used to control each stream independently.

        :Args:

            map_list: list of SLMap objects, optional
                Users defined set of parameters scaling. There is default
                scaling for each object that accept `ctrl` method.
            title: string, optional
                Title of the window. If none is provided, the name of the
                class is used.
        """
        '''
        if map_list is None:
            map_list = obj._map_list
        if map_list == []:
            clsname = obj.__class__.__name__
            print("There are no controls for %s object." % clsname)
            return
        '''
        ctrl = PyoObjectControl.produce(obj, map_list, title)
        self.drawables.append(ctrl)
