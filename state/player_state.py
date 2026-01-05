from .relic import Relic
from .potion import Potion
from .card import Card

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
        deck = [Card.from_dict(card) for card in data.get('deck', [])]
        potions = [
            Potion.from_dict(potion) 
            for potion in data.get('potions', []) 
            if potion.get('id') != 'Potion Slot'
        ]

        return cls(current_hp, max_hp, gold, relics, deck, potions)