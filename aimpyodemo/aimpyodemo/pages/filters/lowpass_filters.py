from pyo import *

from .. import Page


class LowpassFilters(Page):
    """
    01-lowpass-filters.py - The effect of the order of a filter.

    For this first example about filtering, we compare the frequency
    spectrum of three common lowpass filters.

    - Tone : IIR first-order lowpass
    - ButLP : IIR second-order lowpass (Butterworth)
    - MoogLP : IIR fourth-order lowpass (+ resonance as an extra parameter)

    Complementary highpass filters for the Tone and ButLP objects are Atone
    and ButHP. Another common highpass filter is the DCBlock object, which
    can be used to remove DC component from an audio signal.

    The next example will present bandpass filters.

    """

    def do_reset(self):
        gui = self.gui
        # White noise generator
        n = Noise(0.5)

        # Common cutoff frequency control
        freq = Sig(1000)
        gui.ctrl(freq, [SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

        # Three different lowpass filters
        tone = Tone(n, freq)
        butlp = ButLP(n, freq)
        mooglp = MoogLP(n, freq)

        # Interpolates between input objects to produce a single output
        self.sel = sel = Selector([tone, butlp, mooglp])
        gui.ctrl(sel, title="Filter selector (0=Tone, 1=ButLP, 2=MoogLP)")

        # Displays the spectrum contents of the chosen source
        gui.spectrum(sel)


    def do_start(self):
        self.sel.out()
