
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
