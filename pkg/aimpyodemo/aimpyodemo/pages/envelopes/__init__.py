from .data_signal_conversion import DataSignalConversion
from .linear_ramp import LinearRamp
from .exponential_ramp import ExponentialRamp
from .simple_envelopes import SimpleEnvelopes
from .breakpoints_functions import BreakpointsFunctions

def install(app):
    app.add_page(DataSignalConversion, "envelopes")
    app.add_page(LinearRamp, "envelopes")
    app.add_page(ExponentialRamp, "envelopes")
    app.add_page(SimpleEnvelopes, "envelopes")
    app.add_page(BreakpointsFunctions, "envelopes")
