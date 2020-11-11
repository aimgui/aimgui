from pyo import *

from .. import Page


class ExponentialRamp(Page):
    """
    03-exponential-ramp.py - Exponential portamento with rising and falling times.

    The Port object is designed to lowpass filter an audio signal with
    different coefficients for rising and falling signals. A lowpass
    filter is a good and efficient way of creating an exponential ramp
    from a signal containing abrupt changes. The rising and falling
    coefficients are controlled in seconds.

    """

    def do_reset(self):
        gui = self.gui
        # 2 seconds linear ramp starting at 0.0 and ending at 0.3.
        amp = SigTo(value=0.3, time=2.0, init=0.0)

        # Pick a new value four times per second.
        pick = Choice([200, 250, 300, 350, 400], freq=4)

        # Print the chosen frequency
        pp = Print(pick, method=1, message="Frequency")

        # Add an exponential portamento on an audio target and detune a second frequency.
        # Sharp attack for rising notes and long release for falling notes.
        freq = Port(pick, risetime=0.001, falltime=0.25, mul=[1, 1.005])
        # Play with portamento times.
        gui.ctrl(freq)

        # Play a simple wave.
        self.sig = RCOsc(freq, sharp=0.7, mul=amp)


    def do_start(self):
        self.sig.out()
