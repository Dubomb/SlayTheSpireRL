import sys
import json
import time

class GameManager:
    def __init__(self, command_cooldown=1.5):
        self.send_command('ready')
        self.command_cooldown = command_cooldown
    
    def send_command(self, command):
        print(command)
        sys.stdout.flush()
    
    def start(self, player_class, ascension='', seed=''):
        self.send_command(f'start {player_class} {ascension} {seed}')
    
    # potion_index, target_index are 0-indexed
    def use_potion(self, potion_index, target_index=''):
        self.send_command(f'potion use {potion_index} {target_index}')

    # potion_index is 0-indexed
    def discard_potion(self, potion_index):
        self.send_command(f'potion discard {potion_index}')
    
    # card_index, target_index are 0-indexed
    def play_card(self, card_index, target_index=''):
        self.send_command(f'play {card_index} {target_index}')
    
    def end_turn(self):
        self.send_command('end')

    def request_state(self):
        self.send_command('state')