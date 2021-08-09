from .process_spawning import ProcessSpawning
from .sharing_audio import SharingAudio
from .synchronization import Synchronization
from .data_control import DataControl

def install(app):
    app.add_page(ProcessSpawning, "multicore")
    app.add_page(SharingAudio, "multicore")
    app.add_page(Synchronization, "multicore")
    app.add_page(DataControl, "multicore")
