class {ENGINE_NAME}:

    def __init__(self):
        self.checkpoint = "1101"
        self.status_state = "ONLINE"

    def status(self):

        return {
            "engine": "{ENGINE_NAME}",
            "checkpoint": self.checkpoint,
            "status": self.status_state
        }
