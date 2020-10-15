from array import array
from random import random
from math import sin

import aimgui

from aimdemo.page import Page


class PlotHistogramPage(Page):
    def reset(self):
        self.values = array('f', [random() for _ in range(20)])

    def draw(self):
        aimgui.begin(self.title)
        aimgui.plot_histogram("histogram(random())", self.values)
        aimgui.end()

class PlotLinesPage(Page):
    def reset(self):
        self.values = array('f', [sin(x * 0.1) for x in range(100)])

    def draw(self):
        aimgui.begin(self.title)
        aimgui.plot_lines("Sin(t)", self.values)
        aimgui.end()

def install(app):
    app.add_page(PlotHistogramPage, "plothistogram", "Plot - Histogram")
    app.add_page(PlotLinesPage, "plotlines", "Plot - Lines")
