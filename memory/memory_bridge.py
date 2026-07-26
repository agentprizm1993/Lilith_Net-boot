
class MemoryBridge:

    def __init__(self, nexus):
        self.nexus = nexus

    def remember(self, key, value):
        self.nexus.save(key, value)
        return f"Saved: {key}"

    def recall(self, key):
        return self.nexus.get(key)
