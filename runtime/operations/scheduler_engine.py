import json
from datetime import datetime
from pathlib import Path


class SchedulerEngine:

    def __init__(self):

        self.name = "Scheduler Engine"
        self.version = "2.0"
        self.status = "ONLINE"

        self.schedule_file = Path(
            "runtime/operations/schedule.json"
        )

        self.initialize()


    def initialize(self):

        self.schedule_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.schedule_file.exists():

            with open(
                self.schedule_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def schedule_task(
        self,
        mission,
        action
    ):

        with open(
            self.schedule_file,
            "r"
        ) as file:

            tasks = json.load(file)


        task = {

            "id": len(tasks) + 1,

            "mission": mission,

            "action": action,

            "status": "QUEUED",

            "created":
                datetime.now().isoformat()

        }


        tasks.append(task)


        with open(
            self.schedule_file,
            "w"
        ) as file:

            json.dump(
                tasks,
                file,
                indent=4
            )


        return task


    def update_status(
        self,
        task_id,
        status
    ):

        with open(
            self.schedule_file,
            "r"
        ) as file:

            tasks = json.load(file)


        for task in tasks:

            if task["id"] == task_id:

                task["status"] = status


        with open(
            self.schedule_file,
            "w"
        ) as file:

            json.dump(
                tasks,
                file,
                indent=4
            )


    def report(self):

        with open(
            self.schedule_file,
            "r"
        ) as file:

            return {

                "engine": self.name,

                "version": self.version,

                "status": self.status,

                "tasks": json.load(file)

            }


if __name__ == "__main__":

    scheduler = SchedulerEngine()

    scheduler.schedule_task(
        "Operations Fabric Build",
        "Run validation cycle"
    )

    print(
        scheduler.report()
    )
