class WorkflowEngine:

    def __init__(self):
        self.workflows = []

    def add(self, workflow):

        self.workflows.append(workflow)

    def run(self):

        return "WORKFLOW COMPLETE"

    def status(self):

        return {
            "engine": "Workflow Runtime",
            "workflows": len(self.workflows),
            "status": "ONLINE"
        }
