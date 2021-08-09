from .lowpass_filters import LowpassFilters
from .bandpass_filters import BandpassFilters
from .complex_resonator import ComplexResonator
from .phasing import Phasing
from .convolution_filters import ConvolutionFilters
from .vocoder import VocoderPage
from .hilbert_transform import HilbertTransform

def install(app):
    app.add_page(LowpassFilters, "filters")
    app.add_page(BandpassFilters, "filters")
    app.add_page(ComplexResonator, "filters")
    app.add_page(Phasing, "filters")
    app.add_page(ConvolutionFilters, "filters")
    app.add_page(VocoderPage, "filters")
    app.add_page(HilbertTransform, "filters")
