from runtime.operations.analytics_engine import AnalyticsEngine
from runtime.operations.mission_engine import MissionEngine
from runtime.operations.scheduler_engine import SchedulerEngine
from runtime.operations.operations_bridge import OperationsBridge


class OperationsValidator:

    def __init__(self):

        self.name = "Operations Fabric Validator"
        self.version = "1.0"


    def validate(self):

        results = {}

        try:
            AnalyticsEngine()
            results["Analytics Engine"] = "PASS"

        except Exception as error:
            results["Analytics Engine"] = f"FAIL: {error}"


        try:
            MissionEngine()
            results["Mission Engine"] = "PASS"

        except Exception as error:
            results["Mission Engine"] = f"FAIL: {error}"


        try:
            SchedulerEngine()
            results["Scheduler Engine"] = "PASS"

        except Exception as error:
            results["Scheduler Engine"] = f"FAIL: {error}"


        try:
            OperationsBridge()
            results["Operations Bridge"] = "PASS"

        except Exception as error:
            results["Operations Bridge"] = f"FAIL: {error}"


        results["status"] = (
            "VALIDATED"
            if all(
                value == "PASS"
                for key, value in results.items()
                if key != "status"
            )
            else "FAILED"
        )

        return results


if __name__ == "__main__":

    validator = OperationsValidator()

    print("==============================")
    print(validator.name)
    print("==============================")

    report = validator.validate()

    for item, state in report.items():
        print(f"{item}: {state}")
