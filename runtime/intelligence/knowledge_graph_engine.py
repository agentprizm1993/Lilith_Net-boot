import json
from pathlib import Path


class KnowledgeGraphEngine:

    def __init__(self):
        self.name = "Knowledge Graph Engine"
        self.version = "1.0"
        self.graph_file = Path(
            "runtime/intelligence/knowledge_graph.json"
        )

        self.initialize()

    def initialize(self):

        self.graph_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.graph_file.exists():
            self.save({
                "nodes": {},
                "relationships": []
            })

    def load(self):

        with open(self.graph_file, "r") as file:
            return json.load(file)

    def save(self, data):

        with open(self.graph_file, "w") as file:
            json.dump(
                data,
                file,
                indent=4
            )

    def add_node(self, name, node_type):

        graph = self.load()

        graph["nodes"][name] = {
            "type": node_type
        }

        self.save(graph)

    def add_relationship(
        self,
        source,
        relation,
        target
    ):

        graph = self.load()

        graph["relationships"].append({
            "source": source,
            "relation": relation,
            "target": target
        })

        self.save(graph)

    def report(self):

        return self.load()


if __name__ == "__main__":

    engine = KnowledgeGraphEngine()

    engine.add_node(
        "L.I.L.I.T.H.",
        "Runtime Intelligence"
    )

    engine.add_node(
        "Reasoning Engine",
        "Intelligence Module"
    )

    engine.add_relationship(
        "L.I.L.I.T.H.",
        "uses",
        "Reasoning Engine"
    )

    print(engine.report())
