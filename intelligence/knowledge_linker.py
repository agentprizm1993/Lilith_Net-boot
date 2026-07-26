
class KnowledgeLinker:

    def link(self, concept_a, concept_b):

        return {
            "connection": [
                concept_a,
                concept_b
            ],
            "status": "LINKED"
        }
