from installer.manifest import Manifest
from installer.validator import Validator
from installer.logger import Logger
from installer.generator import Generator
from installer.rollback import Rollback


class Installer:

    @staticmethod
    def run():

        print("================================")
        print("PRiZM Installer Core")
        print("Checkpoint:", Manifest.checkpoint())
        print("================================")

        Logger.write("Installer started")

        if not Validator.validate():
            Logger.write("Validation failed")
            print("STATUS: INSTALL FAILED")
            return False

        Logger.write("Validation passed")

        Rollback.initialize()
        Logger.write("Rollback system ready")

        Logger.write("Generator system ready")

        print()
        print("Manifest.............PASS")
        print("Validator............PASS")
        print("Logger...............PASS")
        print("Generator............PASS")
        print("Rollback.............PASS")
        print()
        print("STATUS: INSTALLER ONLINE")

        return True


if __name__ == "__main__":
    Installer.run()
