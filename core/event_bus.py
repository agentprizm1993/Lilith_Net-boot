class EventBus:

    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

    def publish(self, event_name, data=None):
        listeners = self.listeners.get(event_name, [])

        for callback in listeners:
            callback(data)

    def status(self):
        return {
            "events": list(self.listeners.keys()),
            "listener_count": sum(
                len(items) for items in self.listeners.values()
            )
        }
