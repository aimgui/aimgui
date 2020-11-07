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

    def reset(self):
        #s.amp = 0.1

        # Creates two objects with cool parameters, one per channel.
        self.a = FM()
        self.b = FM()

        # Opens the controller windows.
        a.ctrl(title="Frequency modulation left channel")
        b.ctrl(title="Frequency modulation right channel")

        # If a list of values is given at a particular argument, the ctrl
        # window will show a multislider to set each value separately.

        oscs = Sine([100, 200, 300, 400, 500, 600, 700, 800], mul=0.1).out()
        oscs.ctrl(title="Simple additive synthesis")

        s.gui(locals())

    def play(self):
        self.a.out()
        self.b.out(1)
