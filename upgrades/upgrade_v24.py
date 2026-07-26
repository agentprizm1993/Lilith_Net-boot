from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 45)
print("PRiZM Upgrade Installer")
print("Version: v2.4")
print("Checkpoint: 1101")
print("=" * 45)


def write(path, content):

    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w") as f:
        f.write(content)

    print("[INSTALLED]", path)


capability_router = '''
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
'''

write(
    "capabilities/capability_router.py",
    capability_router
)


capability_command = '''
class CapabilityCommand:

    def __init__(self, router):
        self.router = router


    def run(self, command):

        result = self.router.execute(command)

        print("==============================")
        print("CAPABILITY ROUTING")
        print("==============================")
        print("Request:", result["request"])
        print("Capability:", result["capability"])
        print("Status:", result["status"])
'''

write(
    "commands/capability_command.py",
    capability_command
)


print()
print("=" * 45)
print("PRiZM v2.4 CAPABILITY ROUTING READY")
print("CHECKPOINT: 1101")
print("=" * 45)
