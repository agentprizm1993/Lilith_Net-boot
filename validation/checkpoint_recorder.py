
import json
from datetime import datetime


class CheckpointRecorder:

    def record(self, report):

        data = {
            "timestamp": str(datetime.now()),
            "checkpoint": "1101",
            "validation": report
        }

        with open(
            "validation/checkpoint_log.json",
            "w"
        ) as f:

            json.dump(data, f, indent=4)

        return data
