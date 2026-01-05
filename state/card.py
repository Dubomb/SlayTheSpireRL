class Card:
    def __init__(self, name, uuid, is_playable, cost, upgrades, id, card_type, rarity, requires_target, exhausts, ethereal):
        self.name = name
        self.uuid = uuid
        self.is_playable = is_playable
        self.cost = cost
        self.upgrades = upgrades
        self.id = id
        self.card_type = card_type
        self.rarity = rarity
        self.requires_target = requires_target
        self.exhausts = exhausts
        self.ethereal = ethereal
    
    @classmethod
    def from_dict(cls, data):
        name = data.get('name', '')
        uuid = data.get('uuid', '')
        is_playable = data.get('is_playable', False)
        cost = data.get('cost', 3)
        upgrades = data.get('upgrades', 0)
        id = data.get('id', '')
        card_type = data.get('type', '')
        rarity = data.get('rarity', '')
        requires_target = data.get('has_target', False)
        exhausts = data.get('exhausts', False)
        ethereal = data.get('ethereal', False)
        
        return cls(name, uuid, is_playable, cost, upgrades, id, card_type, rarity, requires_target, exhausts, ethereal)