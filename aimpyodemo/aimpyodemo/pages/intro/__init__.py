from .sine_tone import SinePage
from .parallel_proc import ParallelProcPage
from .serial_proc import SerialProcPage
from .output_channels import OutputChannelsPage

def install(app):
    app.add_page(SinePage, "intro", "sine", "Sine")
    app.add_page(ParallelProcPage, "intro", "parallelproc", "ParallelProc")
    app.add_page(OutputChannelsPage, "intro", "outputchannels", "OutputChannels")
