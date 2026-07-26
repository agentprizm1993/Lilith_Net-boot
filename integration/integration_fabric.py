
class IntegrationFabric:

    def __init__(self):
        self.connections = []


    def connect(self, source, target):

        self.connections.append(
            {
                "source": source,
                "target": target
            }
        )


    def status(self):

        return {
            "connections": len(self.connections),
            "status": "ONLINE"
        }
