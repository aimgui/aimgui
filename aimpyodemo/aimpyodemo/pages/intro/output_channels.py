
from pyo import *

import aimgui

from .. import Page


class OutputChannels(Page):
    """
    05-output-channels.py - Sending signals to different physical outputs.

    The simplest way to choose the output channel where to send the sound
    is to give it as the first argument of the out() method. In fact, the
    signature of the out() method reads as:

    .out(chnl=0, inc=1, dur=0, delay=0)

    `chnl` is the output where to send the first audio channel (stream) of
    the object. `inc` is the output increment for other audio channels.
    `dur` is the living duration, in seconds, of the process and `delay`
    is a delay, in seconds, before activating the process. A duration of
    0 means play forever.

    """

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Creates a source (white noise)
        n = Noise()

        # Sends the bass frequencies (below 1000 Hz) to the left
        self.lp = ButLP(n)

        # Sends the high frequencies (above 1000 Hz) to the right
        self.hp = ButHP(n)

    def do_start(self):
        self.lp.out()
        self.hp.out(1)
