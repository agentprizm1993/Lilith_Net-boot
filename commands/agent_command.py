
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
