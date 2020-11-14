from .simple_sequences import SimpleSequences
from .parameters import Parameters
from .instruments import Instruments
from .custom_params import CustomParams
from .complex_sequences import ComplexSequences
from .randoms import Randoms

def install(app):
    app.add_page(SimpleSequences, "events")
    app.add_page(Parameters, "events")
    app.add_page(Instruments, "events")
    app.add_page(CustomParams, "events")
    app.add_page(ComplexSequences, "events")
    app.add_page(Randoms, "events")
