from .flanger import Flanger
from .schroeder_reverb import SchroederReverb
from .fuzz_disto import FuzzDisto
from .ping_pong_delay import PingPongDelay
from .hand_made_chorus import HandMadeChorus
from .hand_made_harmonizer import HandMadeHarmonizer

def install(app):
    app.add_page(Flanger, "effects")
    app.add_page(SchroederReverb, "effects")
    app.add_page(FuzzDisto, "effects")
    app.add_page(PingPongDelay, "effects")
    app.add_page(HandMadeChorus, "effects")
    app.add_page(HandMadeHarmonizer, "effects")
