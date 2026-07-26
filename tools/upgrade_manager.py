import os
import subprocess


class UpgradeManager:

    def __init__(self):
        self.checkpoint = "1101"

    def scan(self):

        folders = [
            "core",
            "engines",
            "config",
            "data",
            "tests",
            "tools"
        ]

        print("PRiZM Structure Scan")

        for folder in folders:
            state = "OK" if os.path.exists(folder) else "MISSING"
            print(f"{folder:<15}{state}")

    def boot(self):

        print("\nRunning PRiZM boot test...\n")

        result = subprocess.run(
            ["python", "main.py"],
            text=True,
            capture_output=True
        )

        print(result.stdout)

        if result.returncode == 0:
            print("BOOT: PASS")
        else:
            print("BOOT: FAILED")


if __name__ == "__main__":

    print("==============================")
    print("PRiZM Upgrade Manager v0.1")
    print("Checkpoint:", "1101")
    print("==============================\n")

    manager = UpgradeManager()
    manager.scan()
    manager.boot()
