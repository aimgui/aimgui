from .read_from_disk import ReadFromDisk
from .read_from_disk_2 import ReadFromDisk2
from .read_from_ram import ReadFromRam
from .record_perf import RecordPerf
from .record_streams import RecordStreams

def install(app):
    app.add_page(ReadFromDisk, "soundfiles", "readfromdisk", "ReadFromDisk")
    app.add_page(ReadFromDisk2, "soundfiles", "readfromdisk2", "ReadFromDisk2")
    app.add_page(ReadFromRam, "soundfiles", "readfromram", "ReadFromRam")
    app.add_page(RecordPerf, "soundfiles", "recordperf", "RecordPerf")
    app.add_page(RecordStreams, "soundfiles", "recordstreams", "RecordStreams")
