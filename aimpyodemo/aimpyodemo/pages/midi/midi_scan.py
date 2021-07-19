from pyo import *

from .. import Page


class MidiScan(Page):
    """
    01-midi-scan.py - Scan for MIDI channels and controller numbers.

    CtlScan and CtlScan2 objects are useful to find controller numbers used
    by your MIDI devices.

    List of MIDI-related functions:

    - pm_count_devices:
        Returns the number of devices found by Portmidi.
    - pm_get_default_input:
        Returns the index number of Portmidi's default input device.
    - pm_get_default_output:
        Returns the index number of Portmidi's default output device.
    - pm_get_input_devices:
        Returns midi input devices (device names, device indexes) found by Portmidi.
    - pm_get_output_devices:
        Returns midi output devices (device names, device indexes) found by Portmidi.
    - pm_list_devices:
        Prints a list of all devices found by Portmidi.

    """

    def create_server(self):
        #self.server = s = Server(audio='jack', duplex=0)
        self.server = s = Server(duplex=0)
        # Give the ID of the desired device (as listed by pm_list_devices()) to the
        # setMidiInputDevice() of the Server. A bigger number than the higher device
        # ID will open all connected MIDI devices.
        s.setMidiInputDevice(1)
        s.boot()

    def do_reset(self):
        # Print the list of available MIDI devices to the console.
        pm_list_devices()

        print("Play with your Midi controllers...")

        # Function called by CtlScan2 object.
        def scanner(ctlnum, midichnl):
            print("MIDI channel: %d, controller number: %d" % (midichnl, ctlnum))


        # Listen to controller input.
        #scan = CtlScan2(scanner, toprint=False)
        self.scan = CtlScan(scanner)

    def do_start(self):
        self.a.out()
