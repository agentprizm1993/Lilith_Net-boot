
class UniversalContextGraph:

    def __init__(self):
        self.connections = []


    def link(self, a, b):

        self.connections.append(
            {
                "from": a,
                "to": b
            }
        )


    def status(self):

        return {
            "links": len(self.connections),
            "state": "ACTIVE"
        }
