from pyo import *

from .. import Page


class SerialProc(Page):
    """
    04-serial-proc.py - Chaining processes on a single source.

    This example shows how to chain processes on a single source.
    Every processing object (ie the ones that modify an audio source) have
    a first argument called "input". This argument takes the audio object
    to process.

    Note the input variable given to each Harmonizer.

    """

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Creates a sine wave as the source to process.
        self.a = a = Sine()

        # Passes the sine wave through an harmonizer.
        self.h1 = h1 = Harmonizer(a)

        # Then the harmonized sound through another harmonizer.
        self.h2 = h2 = Harmonizer(h1)

        # And again...
        self.h3 = h3 = Harmonizer(h2)

        # And again...
        self.h4 = Harmonizer(h3)

    def do_start(self):
        self.a.out()
        self.h1.out()
        self.h2.out()
        self.h3.out()
        self.h4.out()
