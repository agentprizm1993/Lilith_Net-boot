
class EvolutionEngine:

    def __init__(self):
        self.history = []


    def evaluate(self, upgrade, validation):

        result = {
            "upgrade": upgrade,
            "validation": validation,
            "approved": validation == "PASS"
        }

        self.history.append(result)

        return result


    def history_report(self):

        return self.history
