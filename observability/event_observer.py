
class EventObserver:

    def __init__(self):
        self.history = []


    def capture(self, event):

        self.history.append({
            "event": event.name,
            "data": event.data
        })

        print(
            "EVENT:",
            event.name
        )
