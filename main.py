import sys
import time
import traceback

from game_manager import GameManager
from state_manager import StateManager
from state.game_state import GameState
from debug.game_debugger import GameDebugger

def main():
    with GameDebugger('debug_log.txt') as gd:
        gd.log_message('Started!')

        gm = GameManager()
        sm = StateManager()

        while True:
            try:
                gd.log_message('Refreshing state...')
                state = sm.read_state()

                if not state:
                    gd.log_message('No state')
                    continue

                game_state = GameState.from_dict(state)

                gd.log_message(game_state.room_state.player.relics[0].name)
            except Exception as e:
                error = traceback.format_exc()
                gd.log_message(f'ERROR:\n{error}')
                time.sleep(2)


if __name__ == '__main__':
    main()