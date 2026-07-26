
import json
from pathlib import Path


class PRiZMIntegration:

    def __init__(self):

        self.manifest = Path("PRiZM_VERSION.json")


    def status(self):

        if self.manifest.exists():

            with open(self.manifest) as f:
                return json.load(f)

        return {
            "version": "unknown",
            "checkpoint": "unknown"
        }
