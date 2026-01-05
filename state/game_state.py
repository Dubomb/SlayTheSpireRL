import json
from .room_state import RoomState
from .player_state import PlayerState
from debug.game_debugger import GameDebugger

class GameState:
    def __init__(self, available_commands, ready, in_game, room_state, player_state):
        self.available_commands = available_commands
        self.ready = ready
        self.in_game = in_game
        self.room_state = room_state
        self.player_state = player_state

    @classmethod
    def from_dict(cls, data):
        available_commands = data.get('available_commands', [])
        is_ready = data.get('ready_for_command', False)
        in_game = data.get('in_game', False)

        room_state = None
        player_state = None
        if in_game and 'game_state' in data:
            room_state = RoomState.from_dict(data['game_state'])
            player_state = PlayerState.from_dict(data['game_state'])

        return cls(list(available_commands), bool(is_ready), bool(in_game), room_state, player_state)