class Kernel:

    def boot(self):
        print("================================")
        print("PRiZM v0.1")
        print("Checkpoint: 1101")
        print("================================")

        services = [
            "Kernel",
            "Registry",
            "Trust",
            "Integrity",
            "Memory",
            "Observability"
        ]

        for service in services:
            print(f"{service:<20} ONLINE")

        print()
        print("STATUS: READY")
        print("CHECKPOINT: 1101")
