import numpy as np

import aimgui
import aimplot

from aimplotdemo.page import Page


class LinePlotPage(Page):
    def reset(self):
        self.a = np.random.rand(10)
        self.b = np.random.rand(10)

    def draw(self):
        aimgui.set_next_window_pos((16, 32), aimgui.COND_FIRST_USE_EVER )
        aimgui.set_next_window_size((512, 512), aimgui.COND_FIRST_USE_EVER )

        aimgui.begin(self.title)

        if aimplot.begin_plot("My Plot"):
            aimplot.plot_line("A", self.a, 10)
            aimplot.plot_line("B", self.b, 10)
            #aimplot.plot_bars("B", self.values, 10)
            aimplot.end_plot()

        aimgui.end()

def install(app):
    app.add_page(LinePlotPage, "line", "Line Plot")
