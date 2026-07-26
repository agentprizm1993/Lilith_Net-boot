class HealthMonitor:

    def __init__(self):
        self.checkpoint = "1101"
        self.status = "ONLINE"

    def check(self):

        return {
            "engine": "Health Monitor",
            "checkpoint": self.checkpoint,
            "status": self.status
        }

    def report(self):

        print("Health Monitor        ONLINE")
        print("Checkpoint:", self.checkpoint)
