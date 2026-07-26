class Test:

    def __init__(self):
        self.checkpoint = "1101"
        self.status_state = "ONLINE"

    def status(self):

        return {
            "engine": "Test",
            "checkpoint": self.checkpoint,
            "status": self.status_state
        }
