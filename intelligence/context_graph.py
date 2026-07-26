
class ContextGraph:

    def __init__(self):
        self.links = []


    def connect(self, source, target):

        self.links.append(
            {
                "source": source,
                "target": target
            }
        )


    def get_links(self):

        return self.links
