from pyo import *

import aimgui

from .. import Page


class FixedControl(Page):
    """
    01-fixed-control.py - Number as argument.

    Audio objects behaviour can be controlled by passing
    value to their arguments at initialization time.

    """

    def reset(self):
        # Sets fundamental frequency
        freq = 440

        # Approximates a triangle waveform by adding odd harmonics with
        # amplitude proportional to the inverse square of the harmonic number.
        self.h1 = Sine(freq=freq, mul=1)
        self.h2 = Sine(freq=freq * 3, phase=0.5, mul=1.0 / pow(3, 2))
        self.h3 = Sine(freq=freq * 5, mul=1.0 / pow(5, 2))
        self.h4 = Sine(freq=freq * 7, phase=0.5, mul=1.0 / pow(7, 2))
        self.h5 = Sine(freq=freq * 9, mul=1.0 / pow(9, 2))
        self.h6 = Sine(freq=freq * 11, phase=0.5, mul=1.0 / pow(11, 2))

        # Displays the final waveform
        #sp = Scope(self.h1 + self.h2 + self.h3 + self.h4 + self.h5 + self.h6)

    def play(self):
        self.h1.out()
        self.h2.out()
        self.h3.out()
        self.h4.out()
        self.h5.out()
        self.h6.out()
