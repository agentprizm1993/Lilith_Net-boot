
class StatusCommand:

    def __init__(self, integration):
        self.integration = integration


    def execute(self):

        data = self.integration.status()

        print("==============================")
        print("PRiZM SYSTEM STATUS")
        print("==============================")
        print("Version:", data.get("version"))
        print("Checkpoint:", data.get("checkpoint"))
        print("Status:", data.get("status"))
