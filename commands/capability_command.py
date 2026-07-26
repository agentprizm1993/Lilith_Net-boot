
class CapabilityCommand:

    def __init__(self, router):
        self.router = router


    def run(self, command):

        result = self.router.execute(command)

        print("==============================")
        print("CAPABILITY ROUTING")
        print("==============================")
        print("Request:", result["request"])
        print("Capability:", result["capability"])
        print("Status:", result["status"])
