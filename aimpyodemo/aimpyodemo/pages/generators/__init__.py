from .complex_oscs import ComplexOcsPage
from .band_limited_oscs import BandLimitedOcs
from .fm_generators import FmGeneratorsPage
from .noise_generators import NoiseGenerators
from .strange_attractors import StrangeAttractors
from .random_generators import RandomGeneratators

def install(app):
    app.add_page(ComplexOcsPage, "generators", "complexocs", "ComplexOcs")
    app.add_page(BandLimitedOcs, "generators", "bandlimitedocs", "BandLimitedOcs")
    app.add_page(FmGeneratorsPage, "generators", "fmgenerators", "FmGenerators")
    app.add_page(NoiseGenerators, "generators", "noisegenerators", "NoiseGenerators")
    app.add_page(StrangeAttractors, "generators", "strangeattractors", "StrangeAttractors")
    app.add_page(RandomGeneratators, "generators", "randomgenerators", "RandomGeneratators")
