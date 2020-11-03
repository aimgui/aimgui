import time

from pyo import *

import aimgui

from . import Page


class BasicPage(Page):
    def reset(self):
        # FM implements the basic Chowning algorithm
        fm1 = FM(carrier=250, ratio=[1.5, 1.49], index=10, mul=0.3)
        #fm1.ctrl()

        # CrossFM implements a frequency modulation synthesis where the
        # output of both oscillators modulates the frequency of the other one.
        fm2 = CrossFM(carrier=250, ratio=[1.5, 1.49], ind1=10, ind2=2, mul=0.3)
        #fm2.ctrl()

        # Interpolates between input objects to produce a single output
        self.sel = Selector([fm1, fm2]).out(dur=3.)
        #sel.ctrl(title="Input interpolator (0=FM, 1=CrossFM)")
        #time.sleep(3)

    def draw(self):
        aimgui.begin(self.title)

        aimgui.text("Buzzzz...")
        
        aimgui.end()

def install(app):
    app.add_page(BasicPage, "basic", "Basic")