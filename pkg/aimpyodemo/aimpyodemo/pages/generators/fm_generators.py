from pyo import *

from .. import Page


class FmGenerators(Page):
    """
    03-fm-generators.py - Frequency modulation synthesis.

    There two objects in the library that implement frequency
    modulation algorithms. These objects are very simple, although
    powerful. It is also relatively simple to build a custom FM
    algorithm, this will be covered in the tutorials on custom
    synthesis algorithms.

    Use the "voice" slider of the window "Input interpolator" to
    interpolate between the two sources. Use the controller windows
    to change the parameters of the FM algorithms.

    Note what happened in the controller window when we give a
    list of floats to an object's argument.

    """

    def do_reset(self):
        gui = self.gui
        # FM implements the basic Chowning algorithm
        fm1 = FM(carrier=250, ratio=[1.5, 1.49], index=10, mul=0.3)
        gui.ctrl(fm1)

        # CrossFM implements a frequency modulation synthesis where the
        # output of both oscillators modulates the frequency of the other one.
        fm2 = CrossFM(carrier=250, ratio=[1.5, 1.49], ind1=10, ind2=2, mul=0.3)
        gui.ctrl(fm2)

        # Interpolates between input objects to produce a single output
        self.sel = sel = Selector([fm1, fm2])
        gui.ctrl(sel, title="Input interpolator (0=FM, 1=CrossFM)")

        # Displays the spectrum contents of the chosen source
        gui.spectrum(sel)

        #s.gui(locals())

    def do_start(self):
        self.sel.out()
