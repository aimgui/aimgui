from pyo import *

import aimgui

from .. import Page


class ParallelProcPage(Page):
    """
    03-parallel-proc.py - Multiple processes on a single source.

    This example shows how to play different audio objects side-by-side.
    Every processing object (ie the ones that modify an audio source) have
    a first argument called "input". This argument takes the audio object
    to process.

    Note the input variable given to each processing object and the call
    to the out() method of each object that should send its samples to the
    output.

    """

    def reset(self):
        # Creates a sine wave as the source to process.
        a = Sine()

        # Passes the sine wave through an harmonizer.
        self.hr = Harmonizer(a)

        # Also through a chorus.
        self.ch = Chorus(a)

        # And through a frequency shifter.
        self.sh = FreqShift(a)

    def play(self):
        self.hr.out()
        self.ch.out()
        self.sh.out()
