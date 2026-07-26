from core.registry import EngineRegistry
from core.event_bus import EventBus

from engines.trust_engine import TrustEngine
from engines.integrity_engine import IntegrityEngine
from engines.memory_engine import MemoryEngine
from engines.observability import ObservabilityEngine

from plugins.plugin_engine import PluginEngine
from workflows.workflow_engine import WorkflowEngine


class Kernel:

    def __init__(self):
        self.registry = EngineRegistry()
        self.event_bus = EventBus()

        self.trust = TrustEngine()
        self.integrity = IntegrityEngine()
        self.memory = MemoryEngine()
        self.observability = ObservabilityEngine()

        self.plugins = PluginEngine()
        self.workflows = WorkflowEngine()


    def boot(self):

        print("================================")
        print("PRiZM v0.6")
        print("Checkpoint: 1101")
        print("================================")

        self.load_engines()

        print()
        print("Event Bus              ONLINE")
        print("Plugin Framework       ONLINE")
        print("Workflow Runtime       ONLINE")
        print("STATUS: OPERATIONAL")
        print("CHECKPOINT: 1101")


    def load_engines(self):

        engines = {
            "Trust Engine": self.trust,
            "Integrity Engine": self.integrity,
            "Memory Engine": self.memory,
            "Observability Engine": self.observability
        }

        for name, engine in engines.items():
            self.registry.register(name, engine)
            print(f"{name:<25} INITIALIZED")
