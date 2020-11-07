from .fixed_control import FixedControl
from .dynamic_control import DynamicControl

def install(app):
    app.add_page(FixedControl, "controls")
    app.add_page(DynamicControl, "controls")
