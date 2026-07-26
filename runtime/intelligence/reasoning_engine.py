class ReasoningEngine:

    def __init__(self):
        self.name = "Reasoning Engine"
        self.version = "1.0"
        self.status = "ONLINE"

    def create_plan(self, semantic_state):

        intent = semantic_state.get(
            "intent",
            "unknown"
        )

        plans = {

            "creation_request": [
                "analyze requirements",
                "design architecture",
                "implement upgrade",
                "validate system"
            ],

            "system_query": [
                "collect system state",
                "generate report"
            ],

            "runtime_command": [
                "verify command",
                "execute runtime action"
            ]
        }

        return {
            "engine": self.name,
            "version": self.version,
            "intent": intent,
            "plan": plans.get(
                intent,
                ["analyze unknown request"]
            )
        }


if __name__ == "__main__":

    engine = ReasoningEngine()

    test = {
        "intent": "creation_request"
    }

    print(
        engine.create_plan(test)
    )
