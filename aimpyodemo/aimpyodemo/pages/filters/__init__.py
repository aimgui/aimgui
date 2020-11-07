from .lowpass_filters import LowpassFilters

def install(app):
    app.add_page(LowpassFilters, "filters")
