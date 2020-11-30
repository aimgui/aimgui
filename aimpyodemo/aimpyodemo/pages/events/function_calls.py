
import random

from pyo import *

from .. import Page


class FunctionCalls(Page):
    """
    08-function-calls.py - Using custom algorithms with python function calls.

    **EventCall** ::

        EventCall(function, *args, occurrences=inf, stopEventsWhenDone=True)

    EventCall calls a function, with any number of arguments (\*args) and uses
    its return value for the given parameter. The example below use a function
    from the random module, *randrange*, with arguments and a user-defined
    function, without argument, to create a rising, then falling, amplitude curve.

    """

    def do_reset(self):
        self.db = -30
        self.dir = 1


        def riseFallAmp():
            "Rises and falls amplitude between -30 and -3 dB, 1 db at the time."
            self.db += self.dir
            if self.db >= -3:
                self.dir = -1
            elif self.db < -30:
                self.dir = 1
            return self.db


        # Midi notes are chosen randomly with a function from the random module,
        # while the amplitude change according to the riseFallAmp function's output.
        self.e = Events(
            midinote=EventCall(random.randrange, 48, 72, 3),
            beat=1 / 4.0,
            db=EventCall(riseFallAmp),
            attack=0.001,
            decay=0.05,
            sustain=0.5,
            release=0.005,
        )

    def do_start(self):
        self.e.play()
