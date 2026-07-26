import json
from datetime import datetime
from pathlib import Path


class MissionEngine:

    def __init__(self):

        self.name = "Mission Engine"
        self.version = "2.0"
        self.status = "ONLINE"

        self.mission_file = Path(
            "runtime/operations/missions.json"
        )

        self.initialize()


    def initialize(self):

        self.mission_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.mission_file.exists():

            with open(
                self.mission_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    def create_mission(
        self,
        name,
        objective
    ):

        with open(
            self.mission_file,
            "r"
        ) as file:

            missions = json.load(file)


        mission = {

            "id": len(missions) + 1,

            "name": name,

            "objective": objective,

            "status": "CREATED",

            "created":
                datetime.now().isoformat()

        }


        missions.append(mission)


        with open(
            self.mission_file,
            "w"
        ) as file:

            json.dump(
                missions,
                file,
                indent=4
            )


        return mission


    def update_status(
        self,
        mission_id,
        status
    ):

        with open(
            self.mission_file,
            "r"
        ) as file:

            missions = json.load(file)


        for mission in missions:

            if mission["id"] == mission_id:

                mission["status"] = status


        with open(
            self.mission_file,
            "w"
        ) as file:

            json.dump(
                missions,
                file,
                indent=4
            )


    def report(self):

        with open(
            self.mission_file,
            "r"
        ) as file:

            return {

                "engine": self.name,

                "version": self.version,

                "status": self.status,

                "missions": json.load(file)

            }


if __name__ == "__main__":

    engine = MissionEngine()

    engine.create_mission(
        "Operations Fabric Build",
        "Complete integrated operations subsystem"
    )

    print(
        engine.report()
    )
