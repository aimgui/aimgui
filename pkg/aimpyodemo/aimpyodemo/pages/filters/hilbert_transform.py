from pyo import *

from .. import Page


class ComplexMod:
    """
    Complex modulation used to shift the frequency
    spectrum of the input sound.
    """

    def __init__(self, hilb, freq):
        # Quadrature oscillator (sine, cosine).
        self._quad = Sine(freq, [0, 0.25])
        # real * cosine.
        self._mod1 = hilb["real"] * self._quad[1]
        # imaginary * sine.
        self._mod2 = hilb["imag"] * self._quad[0]
        # Up shift corresponds to the sum frequencies.
        self._up = (self._mod1 + self._mod2) * 0.7

    def out(self, chnl=0):
        self._up.out(chnl)
        return self


class HilbertTransform(Page):
    """
    07-hilbert-transform.py - Barberpole-like phasing effect.

    This example uses two frequency shifters (based on complex
    modulation) linearly shifting the frequency content of a sound.

    Frequency shifting is similar to ring modulation, except the
    upper and lower sidebands are separated into individual outputs.

    """

    def do_reset(self):
        # Large spectrum source.
        src = PinkNoise(0.2)

        # Apply the Hilbert transform.
        hilb = Hilbert(src)

        # LFOs controlling the amount of frequency shifting.
        lf1 = Sine(0.03, mul=6)
        lf2 = Sine(0.05, mul=6)

        # Stereo Single-Sideband Modulation.
        self.wetl = ComplexMod(hilb, lf1)
        self.wetr = ComplexMod(hilb, lf2)

        # Mixed with the dry sound.
        self.dry = src.mix(2)


    def do_start(self):
        self.wetl.out()
        self.wetr.out(1)
        self.dry.out()
