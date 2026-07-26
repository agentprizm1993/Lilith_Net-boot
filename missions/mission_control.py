
class MissionControl:

    def __init__(self):
        self.missions = []


    def create(self, mission):

        self.missions.append(mission)

        return {
            "mission": mission,
            "status": "ACTIVE"
        }
