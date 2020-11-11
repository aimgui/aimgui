import random

from pyo import *

from .. import Page


class ComplexResonator(Page):
    """
    03-complex-resonator.py - Filtering by mean of a complex multiplication.

    ComplexRes implements a resonator derived from a complex
    multiplication, which is very similar to a digital filter.

    It is used here to create a rhythmic chime with varying resonance.

    """

    def do_reset(self):
        # Six random frequencies.
        freqs = [random.uniform(1000, 3000) for i in range(6)]

        # Six different plucking speeds.
        self.pluck = pluck = Metro([0.9, 0.8, 0.6, 0.4, 0.3, 0.2])

        # LFO applied to the decay of the resonator.
        decay = Sine(0.1).range(0.01, 0.15)

        # Six ComplexRes filters.
        self.rezos = rezos = ComplexRes(pluck, freqs, decay, mul=5)

        # Change chime frequencies every 7.2 seconds
        def new():
            freqs = [random.uniform(1000, 3000) for i in range(6)]
            rezos.freq = freqs


        self.pat = Pattern(new, 7.2)


    def do_start(self):
        self.pluck.play()
        self.rezos.out()
        self.pat.play()