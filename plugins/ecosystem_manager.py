
class EcosystemManager:

    def __init__(self):
        self.plugins = []


    def register(self, plugin):

        self.plugins.append(plugin)


    def status(self):

        return {
            "plugins": self.plugins,
            "state": "ONLINE"
        }
