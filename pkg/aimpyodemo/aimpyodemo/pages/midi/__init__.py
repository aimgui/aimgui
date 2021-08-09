from .midi_scan import MidiScan
from .notein_object import NoteinObject
from .midi_envelope import MidiEnvelope
from .simple_midi_synth import SimpleMidiSynth
from .control_change import ControlChange
from .midi_out import MidiOut
from .midifile_with_mido import MidifileWithMido

def install(app):
    app.add_page(MidiScan, "midi")
    app.add_page(NoteinObject, "midi")
    app.add_page(MidiEnvelope, "midi")
    app.add_page(SimpleMidiSynth, "midi")
    app.add_page(ControlChange, "midi")
    app.add_page(MidiOut, "midi")
    app.add_page(MidifileWithMido, "midi")
