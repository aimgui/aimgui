import random

from pyo import *

from .. import Page


class PingPongDelay(Page):
    """
    04-ping-pong-delay.py - Stereo ping-pong delay.

    A stereo ping-pong delay is when you use two delays, one hard left and the
    other hard right, and the delays alternate. 

    This exemple illustrates how we can pass the signal of a first object to
    the input of a second even if the first object does not exist yet when the
    second is created.
    
    """

    def reset(self):
        s = self.server
        gui = self.gui
        #s = Server(duplex=0).boot()

        # Compute the duration, in seconds, of one buffer size.
        buftime = s.getBufferSize() / s.getSamplingRate()

        # Delay parameters
        delay_time_l = Sig(0.125)  # Delay time for the left channel delay.
        gui.ctrl(delay_time_l, title="delay time")
        delay_feed = Sig(0.75)  # Feedback value for both delays.
        gui.ctrl(delay_feed, title="delay feed")

        # Because the right delay gets its input sound from the left delay, while
        # it is computed before (to send its output sound to the left delay), it
        # will be one buffer size late. To compensate this additional delay on the
        # right, we substract one buffer size from the real delay time.
        delay_time_r = Sig(delay_time_l, add=-buftime)

        # Setup up a soundfile player.
        sf = SfPlayer(str(self.window.resource_path / "snds" / "alum1.wav")).stop()

        # Send the original sound to both speakers.
        self.sfout = sf.mix(2)

        # Initialize the right delay with zeros as input because the left delay
        # does not exist yet.
        self.right = right = Delay(Sig(0), delay=delay_time_r)

        # Initialize the left delay with the original mono source and the right
        # delay signal (multiplied by the feedback value) as input.
        self.left = left = Delay(sf + right * delay_feed, delay=delay_time_l)

        # One issue with recursive cross-delay is if we set the feedback to
        # 0, the right delay never gets any signal. To resolve this, we add a
        # non-recursive delay, with a gain that is the inverse of the feedback,
        # to the right delay input.
        original_delayed = Delay(sf, delay_time_l, mul=1 - delay_feed)

        # Change the right delay input (now that the left delay exists).
        right.setInput(original_delayed + left * delay_feed)


        def playit():
            "Assign a sound to the player and start playback."
            which = random.randint(1, 4)
            path = "../snds/alum%d.wav" % which
            sf.path = path
            sf.play()


        # Call the function "playit" every second.
        self.pat = Pattern(playit, 1)


    def play(self):
        self.sfout.out()
        self.right.out(1)
        self.left.out()
        self.pat.play()
