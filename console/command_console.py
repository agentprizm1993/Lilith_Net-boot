from runtime.lilith_runtime import LilithRuntime


class CommandConsole:

    def __init__(self):
        self.lilith = LilithRuntime()

    def start(self):

        print("================================")
        print("PRiZM Command Console")
        print("Checkpoint: 1101")
        print("Type 'exit' to quit")
        print("================================")

        while True:

            command = input("PRiZM > ")

            if command.lower() == "exit":
                print("Console Offline")
                break

            if command.strip() == "":
                continue

            self.lilith.execute(command)
