
class IntelligenceMesh:

    def __init__(self):
        self.nodes = {}


    def register(self, name, component):

        self.nodes[name] = component


    def status(self):

        return {
            "nodes": list(self.nodes.keys()),
            "status": "CONNECTED"
        }
