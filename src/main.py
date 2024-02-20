import time
import constants
import keyboard
from macros import Macros
import decorators
from utils import get_timestamp, terminate_program, check_granblue_relink
from utils import format_int, is_on_screen


def main():
    # main constants
    QUEST_DONE = (constants.QUEST_COMPLETE_SCREEN, constants.REPLAY_QUEST)
    check_granblue_relink()
    time_start = time.perf_counter()
    keyboard.on_press_key(
        key="escape", callback=lambda _: terminate_program(time_start)
    )
    runs = 0

    def log(msg: str):
        seconds, minutes, hours = get_timestamp(time_start)
        f_seconds = format_int(seconds)
        f_minutes = format_int(minutes)
        f_hours = format_int(hours)
        timestamp = f"{f_hours}:{f_minutes}:{f_seconds}"
        print(f"[{timestamp}]\t{msg}")

    while True:
        @decorators.loop_run_once
        def on_run_complete():
            """
            Does stuff when a run has been completed
            """
            nonlocal runs
            runs += 1
            log(f"Runs Completed: {runs}")

        # When the user successfully completes the quest
        while is_on_screen(*QUEST_DONE):
            on_run_complete()

            # Select replay option first
            if runs == 1:
                while not is_on_screen(constants.REPEAT_QUEST_FIRST_PROMPT):
                    Macros.left_click()
                
                Macros.repeat_quest()

                while is_on_screen(*QUEST_DONE):
                    Macros.left_click()
            else:
                if is_on_screen(constants.CONTINUE_PLAYING_QUEST):
                    Macros.continue_playing()
                else:
                    Macros.left_click()

        # When the user is requires a revive
        while is_on_screen(constants.HP_ZERO):
            Macros.left_click()


if __name__ == "__main__":
    main()
