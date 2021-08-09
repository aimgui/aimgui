from .read_from_disk import ReadFromDisk
from .read_from_disk_2 import ReadFromDisk2
from .read_from_ram import ReadFromRam
from .record_perf import RecordPerf
from .record_streams import RecordStreams
from .record_table import RecordTable

def install(app):
    app.add_page(ReadFromDisk, "soundfiles")
    app.add_page(ReadFromDisk2, "soundfiles")
    app.add_page(ReadFromRam, "soundfiles")
    app.add_page(RecordPerf, "soundfiles")
    app.add_page(RecordStreams, "soundfiles")
    app.add_page(RecordTable, "soundfiles")
