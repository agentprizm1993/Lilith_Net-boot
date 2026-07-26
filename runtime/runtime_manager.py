from runtime.service_registry import ServiceRegistry


class RuntimeManager:

    def __init__(self):
        ServiceRegistry.initialize()

    def start_service(self, name):
        ServiceRegistry.register(
            name,
            "ONLINE"
        )

    def stop_service(self, name):
        ServiceRegistry.register(
            name,
            "OFFLINE"
        )

    def boot(self):
        print("==============================")
        print("PRiZM Runtime Manager")
        print("==============================")

        self.start_service(
            "Module Loader"
        )

        self.start_service(
            "Service Registry"
        )

        print("Runtime services initialized")
