import json
import os


class MemoryEngine:

    def __init__(self):
        self.file = "data/prizm_memory.json"

    def save(self, key, value):

        memory = {}

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                memory = json.load(f)

        memory[key] = value

        with open(self.file, "w") as f:
            json.dump(memory, f, indent=4)

        return True

    def load(self):

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)

        return {}

    def status(self):

        return {
            "engine": "Memory Engine",
            "storage": self.file,
            "status": "ONLINE"
        }
