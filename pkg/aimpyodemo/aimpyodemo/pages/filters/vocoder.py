import random

from pyo import *

from .. import Page


class VocoderPage(Page):
    """
    06-vocoder.py - Analysis/resynthesis vocoder effect.

    A vocoder is an analysis/resynthesis process that
    uses the spectral envelope of a first sound to shape
    the spectrum of a second sound. Usually (for the best
    results) the first sound should present a dynamic
    spectrum (for both frequencies and amplitudes) and the
    second sound should contain a rich and stable spectrum.

    In this example, LFOs are applied to every dynamic argument
    of the Vocoder object to show the range of sound effects
    the user can get with a vocoder.

    """

    def do_reset(self):
        # First sound - dynamic spectrum.
        spktrm = SfPlayer(str(self.resource_path / "snds" / "baseballmajeur_m.aif"), speed=[1, 1.001], loop=True)

        # Second sound - rich and stable spectrum.
        excite = Noise(0.2)

        # LFOs to modulate every parameters of the Vocoder object.
        lf1 = Sine(freq=0.1, phase=random.random()).range(60, 100)
        lf2 = Sine(freq=0.11, phase=random.random()).range(1.05, 1.5)
        lf3 = Sine(freq=0.07, phase=random.random()).range(1, 20)
        lf4 = Sine(freq=0.06, phase=random.random()).range(0.01, 0.99)

        self.voc = Vocoder(spktrm, excite, freq=lf1, spread=lf2, q=lf3, slope=lf4, stages=32)


    def do_start(self):
        self.voc.out()
