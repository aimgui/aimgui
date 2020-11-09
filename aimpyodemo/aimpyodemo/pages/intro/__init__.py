from .sine_tone import SineTone
from .parallel_proc import ParallelProc
from .serial_proc import SerialProc
from .output_channels import OutputChannels

def install(app):
    app.add_page(SineTone, "intro")
    app.add_page(ParallelProc, "intro")
    app.add_page(SerialProc, "intro")
    app.add_page(OutputChannels, "intro")
