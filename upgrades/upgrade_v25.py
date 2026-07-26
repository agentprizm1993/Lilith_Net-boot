from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 45)
print("PRiZM Upgrade Installer")
print("Version: v2.5")
print("Checkpoint: 1101")
print("=" * 45)


def write(path, content):

    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w") as f:
        f.write(content)

    print("[INSTALLED]", path)


event_system = '''
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
'''

write(
    "core/event_system.py",
    event_system
)


observer = '''
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
'''

write(
    "observability/event_observer.py",
    observer
)


print()
print("=" * 45)
print("PRiZM v2.5 EVENT INTELLIGENCE READY")
print("CHECKPOINT: 1101")
print("=" * 45)
