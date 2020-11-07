from .complex_oscs import ComplexOcs
from .band_limited_oscs import BandLimitedOcs
from .fm_generators import FmGenerators
from .noise_generators import NoiseGenerators
from .strange_attractors import StrangeAttractors
from .random_generators import RandomGeneratators

def install(app):
    app.add_page(ComplexOcs, "generators")
    app.add_page(BandLimitedOcs, "generators")
    app.add_page(FmGenerators, "generators")
    app.add_page(NoiseGenerators, "generators")
    app.add_page(StrangeAttractors, "generators")
    app.add_page(RandomGeneratators, "generators")
