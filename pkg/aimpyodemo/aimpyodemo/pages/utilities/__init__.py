from .list_to_audio_file import ListToAudioFile
from .get_method import GetMethod
from .set_method import SetMethod
from .buffer_interface import BufferInterface
from .batch_processing import BatchProcessing
from .batch_synthesis import BatchSynthesis

def install(app):
    app.add_page(ListToAudioFile, "utilities")
    app.add_page(GetMethod, "utilities")
    app.add_page(SetMethod, "utilities")
    app.add_page(BufferInterface, "utilities")
    app.add_page(BatchProcessing, "utilities")
    app.add_page(BatchSynthesis, "utilities")
