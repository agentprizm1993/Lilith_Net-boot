
class MemoryFabric:

    def __init__(self):
        self.records = {}


    def store(self, key, value):

        self.records[key] = value


    def recall(self):

        return self.records
