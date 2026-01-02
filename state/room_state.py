from .player_state import PlayerState

class RoomState:
    def __init__(self, room_phase, room_type, floor, player):
        self.room_phase = room_phase
        self.room_type = room_type
        self.floor = floor
        self.player = player
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['room_phase'],
                   data['room_type'],
                   int(data['floor']),
                   PlayerState.from_dict(data))