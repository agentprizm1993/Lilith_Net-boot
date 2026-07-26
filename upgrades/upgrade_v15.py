import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 40)
print("PRiZM Upgrade Installer")
print("Version: v1.5")
print("Checkpoint: 1101")
print("=" * 40)


def write(relative_path, content):

    target = ROOT / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)

    with open(target, "w") as f:
        f.write(content)

    print(f"[OK] {relative_path}")


intent_engine = '''class IntentEngine:

    def resolve(self, command):

        cmd = command.lower().strip()

        if "status" in cmd:
            return "status"

        if "scan" in cmd:
            return "scan"

        if "boot" in cmd:
            return "boot"

        if "remember" in cmd:
            return "remember"

        if cmd in ["hello", "hi"]:
            return "hello"

        return "unknown"
'''

write("engines/intent_engine.py", intent_engine)

print()
print("INSTALL COMPLETE")
print()
print("Next steps:")
print("1. git add .")
print('2. git commit -m "PRiZM v1.5 intent engine"')
print("3. python main.py")
