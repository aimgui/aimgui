from pyo import *

from .. import Page


class ParallelProc(Page):
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

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Creates a sine wave as the source to process.
        a = Sine()

        # Passes the sine wave through an harmonizer.
        self.hr = Harmonizer(a)

        # Also through a chorus.
        self.ch = Chorus(a)

        # And through a frequency shifter.
        self.sh = FreqShift(a)

    def do_start(self):
        self.hr.out()
        self.ch.out()
        self.sh.out()
