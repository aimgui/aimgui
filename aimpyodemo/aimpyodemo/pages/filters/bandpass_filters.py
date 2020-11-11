from pyo import *

from .. import Page


class BandpassFilters(Page):
    """
    02-bandpass-filters.py - Narrowing a bandpass filter bandwidth.

    This example illustrates the difference between a simple IIR second-order
    bandpass filter and a cascade of second-order bandpass filters. A cascade
    of four bandpass filters with a high Q can be used as a efficient resonator
    on the signal.

    """

    def do_reset(self):
        gui = self.gui
        # White noise generator
        n = Noise(0.5)

        # Common cutoff frequency control
        freq = Sig(1000)
        gui.ctrl(freq, [SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

        # Common filter's Q control
        q = Sig(5)
        gui.ctrl(q, [SLMap(0.7, 20, "log", "value", 5)], title="Filter's Q")

        # Second-order bandpass filter
        bp1 = Reson(n, freq, q=q)
        # Cascade of second-order bandpass filters
        bp2 = Resonx(n, freq, q=q, stages=4)

        # Interpolates between input objects to produce a single output
        self.sel = sel = Selector([bp1, bp2])
        gui.ctrl(sel, title="Filter selector (0=Reson, 1=Resonx)")

        # Displays the spectrum contents of the chosen source
        gui.spectrum(sel)


    def do_start(self):
        self.sel.out()
