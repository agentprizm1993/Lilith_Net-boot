import json
from datetime import datetime
from pathlib import Path


class AnalyticsEngine:

    def __init__(self):

        self.name = "Analytics Engine"
        self.version = "2.0"
        self.status = "ONLINE"

        self.report_file = Path(
            "runtime/operations/analytics_report.json"
        )

        self.initialize()


    def initialize(self):

        self.report_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.report_file.exists():

            with open(
                self.report_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def capture_event(
        self,
        subsystem,
        state
    ):

        with open(
            self.report_file,
            "r"
        ) as file:

            reports = json.load(file)


        reports.append({

            "timestamp":
                datetime.now().isoformat(),

            "subsystem":
                subsystem,

            "state":
                state,

            "engine":
                self.name,

            "version":
                self.version

        })


        with open(
            self.report_file,
            "w"
        ) as file:

            json.dump(
                reports,
                file,
                indent=4
            )


    def snapshot(self):

        with open(
            self.report_file,
            "r"
        ) as file:

            return {

                "engine": self.name,

                "version": self.version,

                "status": self.status,

                "events": json.load(file)

            }


if __name__ == "__main__":

    analytics = AnalyticsEngine()

    analytics.capture_event(
        "Operations Fabric",
        "INITIALIZED"
    )

    print(
        analytics.snapshot()
    )
