from pathlib import Path
from installer.manifest import Manifest


class Validator:

    REQUIRED_DIRS = [
        "installer",
        "packs",
    ]

    @staticmethod
    def validate():

        root = Path(__file__).resolve().parent.parent

        print("================================")
        print("PRiZM Validation Engine")
        print("Checkpoint:", Manifest.checkpoint())
        print("================================")

        if Manifest.checkpoint() != "1101":
            print("ERROR: Invalid checkpoint.")
            return False

        for directory in Validator.REQUIRED_DIRS:
            if not (root / directory).exists():
                print(f"ERROR: Missing directory: {directory}")
                return False

        print("Manifest.............PASS")
        print("Checkpoint...........PASS")
        print("Directories..........PASS")
        print()
        print("STATUS: VALIDATED")
        return True


if __name__ == "__main__":
    Validator.validate()
