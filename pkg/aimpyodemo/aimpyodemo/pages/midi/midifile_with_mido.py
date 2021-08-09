from pyo import *
from mido import MidiFile

from .. import Page


class MidifileWithMido(Page):
    """
    07-midifile-with-mido.py - Reading a MIDI file with mido and sending the events to pyo.

    This example shows how simple it is to play a MIDI file with mido and send the events
    to an audio synth build with pyo.

    """

    def do_reset(self):
        # A little audio synth to play the MIDI events.
        mid = Notein()
        amp = MidiAdsr(mid["velocity"])
        pit = MToF(mid["pitch"])
        osc = Osc(SquareTable(), freq=pit, mul=amp).mix(1)
        self.rev = STRev(osc, revtime=1, cutoff=4000, bal=0.2)


    def do_start(self):
        s = self.server
        self.rev.out()
        # Opening the MIDI file...
        mid = MidiFile(str(self.resource_path / "snds" / "mapleleafrag.mid"))

        # ... and reading its content.
        for message in mid.play():
            # For each message, we convert it to integer data with the bytes()
            # method and send the values to pyo's Server with the addMidiEvent()
            # method. This method programmatically adds a MIDI message to the
            # server's internal MIDI event buffer.
            s.addMidiEvent(*message.bytes())
