import sys
from genesis_builder import GenesisBuilder


class GenesisOrchestrator:

    def __init__(self):
        self.checkpoint = "1101"

    def deploy(self, version):

        print("==============================")
        print("PRiZM Genesis Orchestrator")
        print("Version:", version)
        print("Checkpoint:", self.checkpoint)
        print("==============================")

        builder = GenesisBuilder()

        builder.build_report()

        print()
        print("GENESIS DEPLOYMENT COMPLETE")
        print("CHECKPOINT:", self.checkpoint)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage:")
        print("python tools/genesis.py deploy version")
        sys.exit()

    command = sys.argv[1]
    version = sys.argv[2]

    if command == "deploy":

        system = GenesisOrchestrator()
        system.deploy(version)
