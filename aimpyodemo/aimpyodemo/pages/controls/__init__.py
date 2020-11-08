from .fixed_control import FixedControl
from .dynamic_control import DynamicControl
from .output_range import OutputRange

def install(app):
    app.add_page(FixedControl, "controls")
    app.add_page(DynamicControl, "controls")
    app.add_page(OutputRange, "controls")
