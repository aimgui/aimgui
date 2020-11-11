from pyo import *

from .. import Page


class BandLimitedOcs(Page):
    """
    02-band-limited-oscs.py - Oscillators whose spectrum is kept under the Nyquist frequency.

    This tutorial presents an object (misnamed LFO but it's too late
    to change its name!) that implements various band-limited waveforms.
    A band-limited signal is a signal that none of its partials exceeds
    the nyquist frequency (sr/2).

    The LFO object, despite its name, can be use as a standard oscillator,
    with very high fundamental frequencies. At lower frequencies (below 20 Hz)
    this object will give a true LFO with various shapes.

    The "type" slider in the controller window lets choose between these
    particular waveforms:

    0. Saw up (default)
    1. Saw down
    2. Square
    3. Triangle
    4. Pulse
    5. Bipolar pulse
    6. Sample and hold
    7. Modulated Sine

    """

    def do_reset(self):
        gui = self.gui
        # Sets fundamental frequency.
        freq = 187.5

        # LFO applied to the `sharp` attribute
        lfo = Sine(0.2, mul=0.5, add=0.5)

        # Various band-limited waveforms
        self.osc = osc = LFO(freq=freq, sharp=lfo, mul=0.4)
        gui.ctrl(osc)

        # Displays the waveform
        sc = gui.scope(osc)

        # Displays the spectrum contents
        sp = gui.spectrum(osc)


    def do_start(self):
        self.osc.out()
