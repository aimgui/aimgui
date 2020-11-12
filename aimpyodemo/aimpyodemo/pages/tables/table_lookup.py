from pyo import *

from .. import Page


class TableLookup(Page):
    """
    08-table-lookup.py - Table as transfer function.

    In computer science, a lookup table is an array that replaces runtime computation
    with a simpler array indexing operation. The savings in terms of processing time
    can be significant, since retrieving a value from memory is often faster than 
    undergoing an "expensive" computation.

    This technic is also used a lot in audio synthesis, where the waveform can be
    pre-computed and stored in a table, then simply readed with a ramp at the desired
    frequency.

    """

    def do_reset(self):
        gui = self.gui
        src = SfPlayer(str(self.resource_path / "snds" / "flute.aif"), loop=True)

        # Arctangent transfer function table.
        table = AtanTable(slope=0.5, size=512)
        gui.view(table)

        # A signal to dynamically control the drive of the transfer function.
        drive = Sig(0.5)

        # We give it True to the dataonly argument when opening the sliders window,
        # otherwise the table would be rewrite way too often.
        gui.ctrl(drive, [SLMap(0, 1, "lin", "value", 0.5, dataOnly=True)], title="Transfer function slope")

        # Lookup reads a table given an audio index lying between -1 and 1.
        # It is especially designed to scan a transfer function with an audio signal.
        self.look = look = Lookup(table, index=src, mul=0.5)

        # Function called to redraw the transfer function.
        def redraw():
            table.slope = drive.get()

        # We call the "redraw" function every time the "drive" value changes.
        self.trig = TrigFunc(Change(drive), function=redraw)

        gui.scope(look)

    def do_start(self):
        self.look.out()
