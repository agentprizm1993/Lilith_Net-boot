
class UnifiedContext:

    def __init__(self):
        self.context = {}


    def update(self, key, value):

        self.context[key] = value


    def read(self):

        return self.context
