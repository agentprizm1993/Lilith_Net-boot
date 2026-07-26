class LilithRuntime:

    def __init__(self):
        self.name = "L.I.L.I.T.H."
        self.version = "1.1"
        self.checkpoint = "1101"
        self.status = "ONLINE"

    def boot(self):
        print("==============================")
        print(f"{self.name} Runtime")
        print(f"Version: {self.version}")
        print(f"Checkpoint: {self.checkpoint}")
        print("==============================")
        print("Runtime Status:", self.status)

    def execute(self, command):

        cmd = command.lower().strip()

        if cmd in ["status", "lilith status"]:
            print("==============================")
            print("L.I.L.I.T.H. STATUS")
            print("==============================")
            print("Runtime:", self.status)
            print("Version:", self.version)
            print("Checkpoint:", self.checkpoint)

        elif cmd in ["boot", "lilith boot"]:
            self.boot()

        elif cmd in ["hello", "hi"]:
            print("Hello. L.I.L.I.T.H. is online.")

        elif cmd in ["scan", "scan system", "lilith scan system"]:
            print("Launching Genesis Scan...")

        else:
            print(f"Unknown command: {command}")
            print("Type 'status', 'scan system', 'boot', or 'hello'.")
