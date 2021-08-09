from pyo import *

from .. import Page


class SineTone(Page):
    """
    02-sine-tone.py - The "hello world" of audio programming!

    This script simply plays a 1000 Hz sine tone.
    """

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Creates a sine wave player.
        # The out() method starts the processing
        # and sends the signal to the output.
        self.a = a = Sine()
        self.gui.ctrl(a, title="Sine Tone")
        sc = self.gui.scope(a)

    def do_start(self):
        self.a.out()
