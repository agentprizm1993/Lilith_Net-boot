import json
from pathlib import Path


class ServiceRegistry:

    REGISTRY_FILE = Path("runtime/services.json")

    @staticmethod
    def initialize():
        ServiceRegistry.REGISTRY_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not ServiceRegistry.REGISTRY_FILE.exists():
            ServiceRegistry.save({})

    @staticmethod
    def load():
        ServiceRegistry.initialize()

        with open(ServiceRegistry.REGISTRY_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):
        with open(ServiceRegistry.REGISTRY_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def register(name, status="OFFLINE"):

        services = ServiceRegistry.load()

        services[name] = {
            "status": status
        }

        ServiceRegistry.save(services)

        print(f"[SERVICE] {name}: {status}")

    @staticmethod
    def status():
        return ServiceRegistry.load()
