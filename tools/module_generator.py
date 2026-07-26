import os
import sys


class ModuleGenerator:

    def __init__(self):
        self.template = "templates/engine_template.py"

    def create_engine(self, name):

        filename = f"engines/{name.lower()}_engine.py"

        if not os.path.exists(self.template):
            print("Template missing")
            return False

        with open(self.template, "r") as file:
            template = file.read()

        class_name = "".join(
            word.capitalize()
            for word in name.split("_")
        )

        content = template.replace(
            "{ENGINE_NAME}",
            class_name
        )

        with open(filename, "w") as file:
            file.write(content)

        print(f"Created: {filename}")

        return True


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python module_generator.py EngineName")
        sys.exit()

    generator = ModuleGenerator()
    generator.create_engine(sys.argv[1])
