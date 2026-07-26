
class IdentityGraph:

    def __init__(self):
        self.nodes = []


    def add(self, identity):

        self.nodes.append(identity)


    def status(self):

        return {
            "identities": self.nodes
        }
