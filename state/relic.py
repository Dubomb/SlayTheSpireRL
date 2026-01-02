class Relic:
    def __init__(self, name, id, counter):
        self.name = name
        self.id = id
        self.counter = counter
    
    @classmethod
    def from_dict(cls, data):
        name = data.get('name', '')
        id = data.get('id', '')
        counter = int(data.get('counter', 0))
        
        return cls(name, id, counter)