import json
from pathlib import Path
from datetime import datetime


class MemoryNexus:

    def __init__(self):

        self.name = "Memory Nexus Engine"
        self.version = "1.0"

        self.memory_file = Path(
            "runtime/memory/memory_store.json"
        )

        self.initialize()


    def initialize(self):

        self.memory_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.memory_file.exists():

            with open(
                self.memory_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def store(
        self,
        category,
        data
    ):

        with open(
            self.memory_file,
            "r"
        ) as file:

            memories = json.load(file)


        memories.append({

            "timestamp":
                datetime.now().isoformat(),

            "category":
                category,

            "data":
                data

        })


        with open(
            self.memory_file,
            "w"
        ) as file:

            json.dump(
                memories,
                file,
                indent=4
            )


    def recall(self):

        with open(
            self.memory_file,
            "r"
        ) as file:

            return json.load(file)



if __name__ == "__main__":

    memory = MemoryNexus()

    memory.store(
        "system_event",
        "Memory Nexus initialized"
    )

    print(
        memory.recall()
    )
