import os
import subprocess


class GenesisBuilder:

    def __init__(self):
        self.checkpoint = "1101"


    def scan(self):

        modules = [
            "core/kernel.py",
            "core/registry.py",
            "core/event_bus.py",
            "engines/trust_engine.py",
            "engines/integrity_engine.py",
            "tools/forge.py"
        ]

        results = {}

        for module in modules:
            results[module] = os.path.exists(module)

        return results


    def boot(self):

        result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout
        }


    def build_report(self):

        print("==============================")
        print("PRiZM Genesis Builder v1.0")
        print("Checkpoint:", self.checkpoint)
        print("==============================")

        scan = self.scan()

        print("\nMODULE SCAN")

        for module, exists in scan.items():
            print(
                f"{module:<35}",
                "READY" if exists else "MISSING"
            )

        print("\nBOOT VALIDATION")

        boot = self.boot()

        if boot["success"]:
            print("BOOT: PASS")
        else:
            print("BOOT: FAILED")

        print("\nGENESIS STATUS")

        if all(scan.values()) and boot["success"]:
            print("GENESIS BUILD READY")
        else:
            print("GENESIS BUILD NEEDS ATTENTION")


if __name__ == "__main__":

    builder = GenesisBuilder()
    builder.build_report()
