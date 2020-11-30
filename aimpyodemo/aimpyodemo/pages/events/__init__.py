from .simple_sequences import SimpleSequences
from .parameters import Parameters
from .instruments import Instruments
from .custom_params import CustomParams
from .complex_sequences import ComplexSequences
from .randoms import Randoms
from .managing_scales import ManagingScales
from .function_calls import FunctionCalls
from .embedding_generators import EmbeddingGenerators
from .arithmetic_ops import ArithmeticOps
from .filters import Filters
from .sharing_values import SharingValues
from .using_audio_objects import UsingAudioObjects
from .post_processing import PostProcessing

def install(app):
    app.add_page(SimpleSequences, "events")
    app.add_page(Parameters, "events")
    app.add_page(Instruments, "events")
    app.add_page(CustomParams, "events")
    app.add_page(ComplexSequences, "events")
    app.add_page(Randoms, "events")
    app.add_page(ManagingScales, "events")
    app.add_page(FunctionCalls, "events")
    app.add_page(EmbeddingGenerators, "events")
    app.add_page(ArithmeticOps, "events")
    app.add_page(Filters, "events")
    app.add_page(SharingValues, "events")
    app.add_page(UsingAudioObjects, "events")
    app.add_page(PostProcessing, "events")
