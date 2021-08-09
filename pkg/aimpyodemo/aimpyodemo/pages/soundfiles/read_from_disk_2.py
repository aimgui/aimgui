import random

from pyo import *

from .. import Page


class ReadFromDisk2(Page):
    """
    02-read-from-disk-2.py - Catching the `end-of-file` signal from the SfPlayer object.

    This example demonstrates how to use the `end-of-file` signal
    of the SfPlayer object to trigger another playback (possibly
    with another sound, another speed, etc.).

    When a SfPlayer reaches the end of the file, it sends a trigger
    (more on trigger later) that the user can retrieve with the
    syntax :

    variable_name["trig"]

    """

    def do_reset(self):
        # Sound bank
        folder = self.resource_path / 'snds'
        sounds = ["alum1.wav", "alum2.wav", "alum3.wav", "alum4.wav"]

        # Creates the left and right players
        self.sfL = sfL = SfPlayer(str(folder / sounds[0]), speed=1, mul=0.5)
        self.sfR = sfR = SfPlayer(str(folder / sounds[0]), speed=1, mul=0.5)

        # Function to choose a new sound and a new speed for the left player
        def newL():
            sfL.path = str(folder / sounds[random.randint(0, 3)])
            sfL.speed = random.uniform(0.75, 1.5)
            sfL.out()


        # The "end-of-file" signal triggers the function "newL"
        self.tfL = TrigFunc(sfL["trig"], newL)

        # Function to choose a new sound and a new speed for the right player
        def newR():
            sfR.path = str(folder / sounds[random.randint(0, 3)])
            sfR.speed = random.uniform(0.75, 1.5)
            sfR.out(1)


        # The "end-of-file" signal triggers the function "newR"
        self.tfR = TrigFunc(sfR["trig"], newR)

    def do_start(self):
        self.sfL.out()
        self.sfR.out()
