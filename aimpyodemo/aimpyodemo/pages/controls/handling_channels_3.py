from pyo import *

from .. import Page


class HandlingChannels3(Page):
    """
    10-handling-channels-3.py - Random multichannel outputs.

    If `chnl` is negative, streams begin at 0, increment the output
    number by inc and wrap around the global number of channels.
    Then, the list of streams is scrambled.

    """

    def do_reset(self):
        # Creates a Server with 8 channels
        #s = Server(nchnls=8).boot()

        amps = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]

        # Generates 8 sine waves with
        # increasing amplitudes
        self.a = Sine(freq=500, mul=amps)



    def do_start(self):
        # Shuffles physical output channels
        self.a.out(chnl=-1)
