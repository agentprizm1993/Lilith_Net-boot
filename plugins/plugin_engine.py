class PluginEngine:

    def __init__(self):
        self.plugins = []

    def register(self, plugin):

        self.plugins.append(plugin)

    def list_plugins(self):

        return self.plugins

    def status(self):

        return {
            "engine": "Plugin Framework",
            "plugins": len(self.plugins),
            "status": "ONLINE"
        }
