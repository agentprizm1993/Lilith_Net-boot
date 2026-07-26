from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 40)
print("PRiZM Upgrade Installer")
print("Version: v1.6")
print("Checkpoint: 1101")
print("=" * 40)


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w") as f:
        f.write(content)

    print("[OK]", path)


memory_nexus = '''import json
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
'''

write("memory/memory_nexus.py", memory_nexus)


print()
print("================================")
print("INSTALLATION COMPLETE")
print("================================")
print("Created:")
print("  memory/memory_nexus.py")
print()
print("Next:")
print("git add .")
print('git commit -m "PRiZM v1.6 memory nexus"')
