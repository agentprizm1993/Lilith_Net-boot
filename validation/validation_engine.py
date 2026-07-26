
class ValidationEngine:

    def __init__(self):
        self.results = []


    def validate(self, component, status=True):

        result = {
            "component": component,
            "status": "PASS" if status else "FAIL"
        }

        self.results.append(result)

        return result


    def report(self):

        return {
            "checkpoint": "1101",
            "results": self.results
        }
