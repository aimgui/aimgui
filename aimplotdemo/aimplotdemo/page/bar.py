import numpy as np

import aimgui
import aimplot

from . import Page


class BarPlotPage(Page):
    def reset(self):
        self.a = np.random.rand(10)
        self.b = np.random.rand(10)

    def draw(self):
        aimgui.begin(self.title)

        if aimplot.begin_plot("My Plot"):
            aimplot.plot_bars("A", self.a, 10)
            aimplot.plot_bars("B", self.b, 10)
            aimplot.end_plot()

        aimgui.end()

class BarPlotH(Page):
    def reset(self):
        self.a = np.random.rand(10)
        self.b = np.random.rand(10)

    def draw(self):
        aimgui.begin(self.title)

        if aimplot.begin_plot("My Plot"):
            aimplot.plot_bars_h("A", self.a, 10)
            aimplot.plot_bars_h("B", self.b, 10)
            aimplot.end_plot()

        aimgui.end()

def install(app):
    app.add_page(BarPlotPage, "bar", "Bar Plot")
    app.add_page(BarPlotH, "bar_h", "Bar Plot - Horizontal")
