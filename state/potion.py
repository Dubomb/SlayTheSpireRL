class Potion:
    def __init__(self, name, id, requires_target, can_use, can_discard):
        self.name = name
        self.id = id
        self.requires_target = requires_target
        self.can_use = can_use
        self.can_discard = can_discard
    
    @classmethod
    def from_dict(cls, data):
        name = data.get('name', '')
        id = data.get('id', '')
        requires_target = bool(data.get('requires_target', False))
        can_use = bool(data.get('can_use', False))
        can_discard = bool(data.get('can_discard', False))
        
        return cls(name, id, requires_target, can_use, can_discard)