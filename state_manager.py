import sys
import json

from debug.game_debugger import GameDebugger

class StateManager:
    def read_state(self):
        try:
            state = sys.stdin.readline()
            return json.loads(state)
        except:
            gd = GameDebugger('error.txt')
            gd.log_message('Error parsing state')
        