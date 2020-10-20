import numpy as np

import aimgui
import aimplot

from . import Page


class ShadedPlotPage(Page):
    def reset(self):
        self.a = np.random.rand(10)
        self.b = np.random.rand(10)

    def draw(self):
        aimgui.begin(self.title)

        if aimplot.begin_plot("My Plot"):
            aimplot.plot_shaded("A", self.a, 10)
            aimplot.plot_shaded("B", self.b, 10)
            aimplot.end_plot()

        aimgui.end()

def install(app):
    app.add_page(ShadedPlotPage, "shaded", "Shaded Plot")
