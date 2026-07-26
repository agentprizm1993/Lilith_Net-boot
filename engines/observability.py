import datetime


class ObservabilityEngine:

    def __init__(self):
        self.events = []

    def record(self, event):

        self.events.append({
            "event": event,
            "time": str(datetime.datetime.now())
        })

    def status(self):

        return {
            "engine": "Observability Engine",
            "events": len(self.events),
            "status": "ONLINE"
        }
