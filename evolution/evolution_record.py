
import json
from datetime import datetime


class EvolutionRecord:

    def save(self, data):

        record = {
            "timestamp": str(datetime.now()),
            "checkpoint": "1101",
            "evolution": data
        }

        with open(
            "evolution/evolution_log.json",
            "w"
        ) as f:
            json.dump(record, f, indent=4)

        return record
