from .envelopes import Envelopes

def install(app):
    app.add_page(Envelopes, "tables")
