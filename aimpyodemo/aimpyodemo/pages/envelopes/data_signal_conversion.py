from pyo import *

from .. import Page


class DataSignalConversion(Page):
    """
    01-data-signal-conversion.py - Conversion from number to audio stream.

    The Stream object is a new type introduced by pyo to represent an
    audio signal as a vector of floats. It is sometimes useful to be
    able to convert simple numbers (python's floats or integers) to
    audio signal or to extract numbers from an audio stream.

    The Sig object converts a number to an audio stream.

    The PyoObject.get() method extracts a float from an audio stream.

    """

    def do_reset(self):
        # A python integer (or float).
        anumber = 100

        # Conversion from number to an audio stream (vector of floats).
        self.astream = Sig(anumber)

    def do_start(self):
        # Use a Print (capital "P") object to print an audio stream.
        pp = Print(self.astream, interval=0.1, message="Audio stream value")

        # Use the get() method to extract a float from an audio stream.
        print("Float from audio stream : ", self.astream.get())
