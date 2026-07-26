
class AgentRegistry:

    def __init__(self):
        self.agents = {
            "Lilith": "Logical Intelligence Core",
            "Atlas": "Infrastructure Agent",
            "Raphael": "Recovery Agent",
            "Uriel": "Security Agent"
        }

    def list_agents(self):
        return self.agents
