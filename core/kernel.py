from core.registry import EngineRegistry


from core.event_bus import EventBus


class Kernel:

    def __init__(self):
        
        self.registry = EngineRegistry()
        self.event_bus = EventBus()

    def boot(self):

        print("================================")
        print("PRiZM v0.2")
        print("Checkpoint: 1101")
        print("================================")

        self.load_engines()

        print()
        print("STATUS: OPERATIONAL")
        print("CHECKPOINT: 1101")


    def load_engines(self):

        engines = [
            "Trust Engine",
            "Integrity Engine",
            "Memory Engine",
            "Observability Engine"
        ]

        for engine in engines:
            self.registry.register(engine, True)
            print(f"{engine:<25} INITIALIZED")
