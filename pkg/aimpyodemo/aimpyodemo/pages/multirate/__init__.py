from .multirate_processing import MultirateProcessing
from .multirate_synthesis import MultirateSynthesis

def install(app):
    app.add_page(MultirateProcessing, "multirate")
    app.add_page(MultirateSynthesis, "multirate")
