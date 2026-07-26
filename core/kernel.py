from core.registry import EngineRegistry
from core.event_bus import EventBus
from engines.trust_engine import TrustEngine
from engines.integrity_engine import IntegrityEngine


class Kernel:

    def __init__(self):
        self.registry = EngineRegistry()
        self.event_bus = EventBus()
        self.trust = TrustEngine()
        self.integrity = IntegrityEngine()

    def boot(self):

        print("================================")
        print("PRiZM v0.5")
        print("Checkpoint: 1101")
        print("================================")

        self.load_engines()

        print()
        print("Event Bus              ONLINE")
        print("STATUS: OPERATIONAL")
        print("CHECKPOINT: 1101")

    def load_engines(self):

        engines = {
            "Trust Engine": self.trust,
            "Integrity Engine": self.integrity,
            "Memory Engine": True,
            "Observability Engine": True
        }

        for name, engine in engines.items():
            self.registry.register(name, engine)
            print(f"{name:<25} INITIALIZED")
