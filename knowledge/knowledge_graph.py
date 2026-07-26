
class KnowledgeGraph:

    def __init__(self):
        self.nodes = []


    def add(self, concept):

        self.nodes.append(concept)


    def status(self):

        return {
            "nodes": self.nodes,
            "state": "CONNECTED"
        }
