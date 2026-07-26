
class GovernanceEngine:

    def __init__(self):
        self.policies = []


    def add_policy(self, policy):

        self.policies.append(policy)


    def evaluate(self, action):

        return {
            "action": action,
            "approved": True,
            "checkpoint": "1101"
        }
