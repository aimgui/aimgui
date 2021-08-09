from pyo import *

from .. import Page


class SimpleSequences(Page):
    """
    01-simple-sequences.py - Looping over a list of values.

    The purpose of the Events framework is to allow the user to generate a
    sequence of events with as few as possible parameters to specify.

    The Events object is at the heart of the framework. An Events object
    compute parameters, generally designed with event generator objects,
    build the events and play the sequence.

    The framework provides a default instrument to play the sequence. We'll
    see later how to build our own synthesizers and use them to play the events.

    EventSeq
    --------

    The basic event generator is EventSeq, which loop over a list of values::

        e = Events(freq = EventSeq([250, 300, 350, 400])).play()

    EventSeq has an "occurrences" keyword, which can be used to fix how many
    times we want to play the sequence of values. The default value is 'inf',
    which means loop forever::

        # This one stops after playing twice the sequence.
        e1 = Events(freq = EventSeq([500, 600, 700, 800], occurrences=2)).play()

    When an Events's parameter is given a list or a single value, it is
    internally converted to an EventSeq. This is the same as the first example::

        e2 = Events(freq = [250, 300, 350, 400])

    """


    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.25

        # Simple infinite sequence.
        self.e = Events(freq=EventSeq([250, 300, 350, 400]))

        # This will play the same note forever.
        self.e3 = Events(freq=200)


    def do_start(self):
        self.e.play()
        self.e3.play()
