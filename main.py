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

                if game_state.player_state and game_state.player_state.potions:
                    gd.log_message(f'Player has {len(game_state.player_state.potions)} potion(s).')

            except Exception as e:
                error = traceback.format_exc()

                gd.log_message(f'ERROR:\n{error}')
                time.sleep(2)


if __name__ == '__main__':
    main()