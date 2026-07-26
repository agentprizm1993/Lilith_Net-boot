from core.registry import EngineRegistry
from core.event_bus import EventBus
from engines.trust_engine import TrustEngine


class Kernel:

    def __init__(self):
        self.registry = EngineRegistry()
        self.event_bus = EventBus()
        self.trust = TrustEngine()

    def boot(self):

        print("================================")
        print("PRiZM v0.4")
        print("Checkpoint: 1101")
        print("================================")

        self.load_engines()

        print()
        print("Event Bus              ONLINE")
        print("STATUS: OPERATIONAL")
        print("CHECKPOINT: 1101")


    def load_engines(self):

        self.registry.register(
            "Trust Engine",
            self.trust
        )

        engines = [
            "Trust Engine",
            "Integrity Engine",
            "Memory Engine",
            "Observability Engine"
        ]

        for engine in engines:
            if engine != "Trust Engine":
                self.registry.register(engine, True)

            print(f"{engine:<25} INITIALIZED")
