
class CommandIntelligence:

    def interpret(self, command):

        cmd = command.lower().strip()

        if "status" in cmd:
            return "status"

        if "agent" in cmd:
            return "agents"

        if "remember" in cmd:
            return "memory"

        if "plugin" in cmd:
            return "plugins"

        if "boot" in cmd:
            return "boot"

        return "unknown"
