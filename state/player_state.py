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
        return cls(int(data['current_hp']),
                   int(data['max_hp']),
                   int(data['gold']),
                   [Relic.from_dict(relic) for relic in data['relics']],
                   data['deck'],
                   data['potions'])