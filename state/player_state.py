from .relic import Relic

class PlayerState:
    def __init__(self, current_hp, max_hp, gold, relics, deck, potions):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.gold = gold
        self.relics = relics
        self.deck = deck
        self.potions = potions
    
    @classmethod
    def from_dict(cls, data):
        current_hp = int(data.get('current_hp', 0))
        max_hp = int(data.get('max_hp', 0))
        gold = int(data.get('gold', 0))
        relics = [Relic.from_dict(relic) for relic in data.get('relics', [])]
        deck = data.get('deck', [])
        potions = data.get('potions', [])

        return cls(current_hp, max_hp, gold, relics, deck, potions)