from pyo import *

import aimgui

from .. import Page


class SinePage(Page):
    """
    02-sine-tone.py - The "hello world" of audio programming!

    This script simply plays a 1000 Hz sine tone.
    """

    def reset(self):
        # Drops the gain by 20 dB.
        #s.amp = 0.1

        # Creates a sine wave player.
        # The out() method starts the processing
        # and sends the signal to the output.
        self.a = Sine()

    def play(self):
        self.a.out()
