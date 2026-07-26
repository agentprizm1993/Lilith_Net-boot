from datetime import datetime
from pathlib import Path
import json


class AuditEngine:

    def __init__(self):

        self.name = "Audit Engine"
        self.version = "1.0"

        self.log_file = Path(
            "runtime/trust/audit_log.json"
        )

        self.initialize()


    def initialize(self):

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.log_file.exists():

            with open(
                self.log_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def record(
        self,
        event,
        status
    ):

        with open(
            self.log_file,
            "r"
        ) as file:

            logs = json.load(file)


        logs.append({

            "timestamp":
                datetime.now().isoformat(),

            "event": event,

            "status": status,

            "engine": self.name,

            "version": self.version

        })


        with open(
            self.log_file,
            "w"
        ) as file:

            json.dump(
                logs,
                file,
                indent=4
            )


    def report(self):

        with open(
            self.log_file,
            "r"
        ) as file:

            return json.load(file)



if __name__ == "__main__":

    audit = AuditEngine()

    audit.record(
        "Trust Fabric startup",
        "VALID"
    )

    print(
        audit.report()
    )
