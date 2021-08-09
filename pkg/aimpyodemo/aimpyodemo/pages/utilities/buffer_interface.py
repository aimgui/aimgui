import numpy as np

from pyo import *

from .. import Page


class BufferInterface(Page):
    """
    Sharing a table with a numpy array using the buffer protocol 

    **04-buffer-interface.py**

    This example shows two things:
        
    1. How to share memory from a PyoTableObject to a numpy array with the
    `getBuffer()` method of the PyoTableObject. Numpy functions can then
    be used to modify the table's content without copying every samples.

    2. How to register a `callback` function, with the `setCallback()` method
    of the Server object, that the server will call at the beginning of
    every processing loop (each `buffersize` samples).

    .. note::

        The numpy module **must** be installed for this example to work.

    """

    def do_reset(self):
        s = self.server
        # Get the length of an audio block.
        bs = s.getBufferSize()

        # Create a table of length `buffer size` and read it in loop.
        t = DataTable(size=bs)
        self.osc = TableRead(t, freq=t.getRate(), loop=True, mul=0.1)

        # Share the table's memory with a numpy array.
        arr = np.asarray(t.getBuffer())


        def process():
            "Fill the array (so the table) with white noise."
            arr[:] = np.random.normal(0.0, 0.5, size=bs)


        # Register the `process` function to be called at the beginning
        # of every processing loop.
        s.setCallback(process)

    def do_start(self):
        self.osc.out()
