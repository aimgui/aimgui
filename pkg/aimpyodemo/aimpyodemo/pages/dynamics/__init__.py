from .dynamic_range import DynamicRange
from .ducking import Ducking
from .gated_verb import GatedVerb
from .rms_tracing import RmsTracing

def install(app):
    app.add_page(DynamicRange, "dynamics")
    app.add_page(Ducking, "dynamics")
    app.add_page(GatedVerb, "dynamics")
    app.add_page(RmsTracing, "dynamics")
