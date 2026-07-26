from pathlib import Path
import importlib


class ModuleLoader:

    MODULE_PATH = Path("runtime/modules")

    @staticmethod
    def initialize():
        ModuleLoader.MODULE_PATH.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def discover():

        ModuleLoader.initialize()

        modules = []

        for file in ModuleLoader.MODULE_PATH.glob("*.py"):
            if file.name != "__init__.py":
                modules.append(file.stem)

        return modules

    @staticmethod
    def load(module_name):

        try:
            module = importlib.import_module(
                f"runtime.modules.{module_name}"
            )

            print(f"[MODULE] {module_name}: LOADED")
            return module

        except Exception as error:
            print(
                f"[MODULE] {module_name}: FAILED - {error}"
            )
            return None
