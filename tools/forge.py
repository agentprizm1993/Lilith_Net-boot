import sys
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.module_generator import ModuleGenerator
from tools.validator import Validator

class PRiZMForge:

    def __init__(self):
        self.checkpoint = "1101"
        self.generator = ModuleGenerator()
        self.validator = Validator()


    def create(self, name):

        print("==============================")
        print("PRiZM Forge v0.9")
        print("Checkpoint:", self.checkpoint)
        print("==============================")

        print("\nGenerating module...\n")

        created = self.generator.create_engine(name)

        if not created:
            print("BUILD FAILED")
            return


        filename = f"engines/{name.lower()}_engine.py"

        print("\nValidating module...\n")

        report = self.validator.validate_file(filename)

        print(report)


        if report["valid"]:
            print("\nFORGE RESULT: PASS")
        else:
            print("\nFORGE RESULT: FAILED")


if __name__ == "__main__":

    forge = PRiZMForge()

    if len(sys.argv) < 3:
        print("Usage:")
        print("python tools/forge.py create engine_name")
        sys.exit()

    command = sys.argv[1]
    name = sys.argv[2]


    if command == "create":
        forge.create(name)
