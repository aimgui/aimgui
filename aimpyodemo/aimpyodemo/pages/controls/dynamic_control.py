from pyo import *

from .. import Page


class DynamicControl(Page):
    """
    02-dynamic-control.py - Graphical control for parameters.

    With pyo, it's easy to quickly try some parameter combination
    with the controller window already configured for each object.
    To open the controller window, just call the ctrl() method on
    the object you want to control.

    """

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Creates two objects with cool parameters, one per channel.
        self.a = a = FM()
        self.b = b = FM()

        gui = self.gui
        gui.clear()
        # Opens the controller windows.
        gui.ctrl(a, title="Frequency modulation left channel")
        gui.ctrl(b, title="Frequency modulation right channel")

        # If a list of values is given at a particular argument, the ctrl
        # window will show a multislider to set each value separately.

        self.oscs = oscs = Sine([100, 200, 300, 400, 500, 600, 700, 800], mul=0.1)
        gui.ctrl(oscs, title="Simple additive synthesis")

        sc = self.gui.scope([a, b, oscs])

    def do_start(self):
        self.a.out()
        self.b.out(1)
        self.oscs.out()
