class TrustEngine:

    def __init__(self):
        self.checkpoint = "1101"

    def validate(self, source):
        return {
            "source": source,
            "verified": True,
            "checkpoint": self.checkpoint,
            "status": "TRUSTED"
        }

    def status(self):
        return {
            "engine": "Trust Engine",
            "checkpoint": self.checkpoint,
            "status": "ONLINE"
        }
