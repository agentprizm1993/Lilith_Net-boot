import json
from pathlib import Path


class MemoryNexus:

    def __init__(self):
        self.file = Path("data/memory.json")

        if not self.file.exists():
            self.file.parent.mkdir(parents=True, exist_ok=True)

            with open(self.file, "w") as f:
                json.dump({}, f)

    def load(self):

        with open(self.file) as f:
            return json.load(f)

    def save(self, key, value):

        memory = self.load()

        memory[key] = value

        with open(self.file, "w") as f:
            json.dump(memory, f, indent=4)

    def get(self, key):

        return self.load().get(key)
