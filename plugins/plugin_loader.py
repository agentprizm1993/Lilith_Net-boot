
import importlib


class PluginLoader:

    def __init__(self):
        self.plugins = {}

    def load(self, name):
        self.plugins[name] = True
        return f"Plugin loaded: {name}"
