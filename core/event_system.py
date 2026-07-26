
class Event:

    def __init__(self, name, data=None):
        self.name = name
        self.data = data


class EventBus:

    def __init__(self):
        self.listeners = {}


    def subscribe(self, event_name, handler):

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(handler)


    def publish(self, event):

        handlers = self.listeners.get(event.name, [])

        for handler in handlers:
            handler(event)

        return {
            "event": event.name,
            "listeners": len(handlers),
            "status": "processed"
        }
