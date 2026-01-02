

class Relic:
    def __init__(self, name, id, counter):
        self.name = name
        self.id = id
        self.counter = counter
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'],
                   data['id'],
                   int(data['counter']))