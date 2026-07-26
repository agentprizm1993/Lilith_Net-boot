import json
from pathlib import Path


class TrustEngine:

    def __init__(self):
        self.name = "Trust Engine"
        self.version = "1.0"
        self.status = "ONLINE"

    def load_identity(self):

        version_file = Path(
            "PRiZM_VERSION.json"
        )

        if version_file.exists():

            with open(version_file, "r") as file:
                return json.load(file)

        return {
            "version": "unknown",
            "checkpoint": "unknown",
            "status": "unknown"
        }


    def verify_checkpoint(self):

        identity = self.load_identity()

        checkpoint = identity.get(
            "checkpoint",
            "unknown"
        )

        if checkpoint == "1101":
            return "VALID"

        return "INVALID"


    def integrity_report(self):

        identity = self.load_identity()

        return {
            "engine": self.name,
            "version": self.version,
            "runtime_status": self.status,
            "checkpoint": identity.get(
                "checkpoint"
            ),
            "integrity": self.verify_checkpoint()
        }


if __name__ == "__main__":

    trust = TrustEngine()

    print(
        trust.integrity_report()
    )
