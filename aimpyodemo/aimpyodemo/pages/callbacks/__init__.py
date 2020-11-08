from .periodic_calls import PeriodicCalls
from .score_calls import ScoreCalls
from .delayed_calls import DelayedCalls

def install(app):
    app.add_page(PeriodicCalls, "callbacks")
    app.add_page(ScoreCalls, "callbacks")
    app.add_page(DelayedCalls, "callbacks")
