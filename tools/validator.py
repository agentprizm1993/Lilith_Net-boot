import os


class Validator:

    def __init__(self):
        self.checkpoint = "1101"


    def validate_file(self, path):

        result = {
            "file": path,
            "exists": False,
            "valid": False,
            "checkpoint": self.checkpoint
        }


        if os.path.exists(path):

            result["exists"] = True

            with open(path, "r") as file:
                content = file.read()

            required = [
                "def __init__",
                "def status",
                "checkpoint"
            ]

            result["valid"] = all(
                item in content
                for item in required
            )


        return result


if __name__ == "__main__":

    validator = Validator()

    report = validator.validate_file(
        "engines/test_engine.py"
    )

    print("==============================")
    print("PRiZM Validator v0.9")
    print("Checkpoint:", report["checkpoint"])
    print("==============================")

    print(report)

    if report["valid"]:
        print("VALIDATION: PASS")
    else:
        print("VALIDATION: FAILED")
