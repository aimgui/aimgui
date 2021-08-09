from .envelopes import Envelopes
from .scrubbing import Scrubbing
from .looping import Looping
from .granulation import Granulation
from .micro_montage import MicroMontage
from .table_stutter import TableStutter
from .moving_points import MovingPoints
from .table_lookup import TableLookup

def install(app):
    app.add_page(Envelopes, "tables")
    app.add_page(Scrubbing, "tables")
    app.add_page(Looping, "tables")
    app.add_page(Granulation, "tables")
    app.add_page(MicroMontage, "tables")
    app.add_page(TableStutter, "tables")
    app.add_page(MovingPoints, "tables")
    app.add_page(TableLookup, "tables")
