
class CapabilityRouter:

    def __init__(self):

        self.capabilities = {
            "diagnostics": "Diagnostics Engine",
            "memory": "Memory Nexus",
            "recovery": "Recovery Engine",
            "forge": "Forge Builder",
            "plugins": "Plugin Loader"
        }


    def route(self, request):

        command = request.lower()

        for capability in self.capabilities:

            if capability in command:
                return self.capabilities[capability]

        return "L.I.L.I.T.H. Core"


    def execute(self, request):

        capability = self.route(request)

        return {
            "request": request,
            "capability": capability,
            "status": "routed"
        }
