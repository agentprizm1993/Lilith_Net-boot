from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 45)
print("PRiZM Upgrade Installer")
print("Version: v2.3")
print("Checkpoint: 1101")
print("=" * 45)


def write(path, content):

    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w") as f:
        f.write(content)

    print("[INSTALLED]", path)


agent_orchestrator = '''
class AgentOrchestrator:

    def __init__(self, registry):
        self.registry = registry


    def select(self, request):

        command = request.lower()

        if "diagnostic" in command:
            return "Raphael"

        if "security" in command:
            return "Uriel"

        if "infrastructure" in command:
            return "Atlas"

        return "Lilith"


    def execute(self, request):

        agent = self.select(request)

        return {
            "agent": agent,
            "request": request,
            "status": "assigned"
        }
'''

write(
    "agents/agent_orchestrator.py",
    agent_orchestrator
)


agent_command = '''
class AgentCommand:

    def __init__(self, orchestrator):
        self.orchestrator = orchestrator


    def run(self, command):

        result = self.orchestrator.execute(command)

        print("==============================")
        print("AGENT ROUTING")
        print("==============================")
        print("Agent:", result["agent"])
        print("Request:", result["request"])
        print("Status:", result["status"])
'''

write(
    "commands/agent_command.py",
    agent_command
)


print()
print("=" * 45)
print("PRiZM v2.3 AGENT ORCHESTRATION READY")
print("CHECKPOINT: 1101")
print("=" * 45)
