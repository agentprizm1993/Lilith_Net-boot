class IntentEngine:

    def resolve(self, command):

        cmd = command.lower().strip()

        if "status" in cmd:
            return "status"

        if "scan" in cmd:
            return "scan"

        if "boot" in cmd:
            return "boot"

        if "remember" in cmd:
            return "remember"

        if cmd in ["hello", "hi"]:
            return "hello"

        return "unknown"
