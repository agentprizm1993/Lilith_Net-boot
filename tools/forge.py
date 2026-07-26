import os
import subprocess
import datetime


class PRiZMForge:

    def __init__(self):
        self.checkpoint = "1101"

    def scan(self):

        required = [
            "core",
            "engines",
            "plugins",
            "workflows",
            "diagnostics",
            "recovery",
            "tools"
        ]

        results = {}

        print("Scanning PRiZM architecture...\n")

        for item in required:
            exists = os.path.exists(item)
            results[item] = exists

            state = "OK" if exists else "MISSING"
            print(f"{item:<20}{state}")

        return results


    def boot_test(self):

        print("\nRunning boot validation...\n")

        result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        return result.returncode == 0


    def report(self):

        print("==============================")
        print("PRiZM Forge v0.8")
        print("Checkpoint:", self.checkpoint)
        print("Time:", datetime.datetime.now())
        print("==============================")

        scan = self.scan()
        boot = self.boot_test()

        print("\nFORGE RESULT")

        if all(scan.values()) and boot:
            print("MASTER BOOT READY")
        else:
            print("BUILD NEEDS ATTENTION")


if __name__ == "__main__":

    forge = PRiZMForge()
    forge.report()
