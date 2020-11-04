from .fixed_control import FixedControlPage

def install(app):
    app.add_page(FixedControlPage, "controls", "fixedcontrol", "FixedControl")
