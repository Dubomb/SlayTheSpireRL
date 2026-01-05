from .player_state import PlayerState

class RoomState:
    def __init__(self, room_phase, room_type, floor):
        self.room_phase = room_phase
        self.room_type = room_type
        self.floor = floor
    
    @classmethod
    def from_dict(cls, data):
        room_phase = data.get('room_phase', '')
        room_type = data.get('room_type', '')
        floor = int(data.get('floor', 0))

        return cls(room_phase, room_type, floor)