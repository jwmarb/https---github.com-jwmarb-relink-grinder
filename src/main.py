import pyautogui
import time
import constants
import keyboard
from macros import Macros
import decorators
from utils import get_timestamp, terminate_program


def main():
    pyautogui.useImageNotFoundException(False)
    time_start = time.perf_counter()
    keyboard.on_press_key(
        key="escape", callback=lambda _: terminate_program(time_start)
    )
    runs = 0

    def log(msg: str):
        seconds, minutes, hours = get_timestamp(time_start)
        print(
            f"[{hours if hours >= 10 else f'0{hours}'}:{minutes if minutes >= 10 else f'0{minutes}'}:{seconds if seconds >= 10 else f'0{seconds}'}]\t{msg}"
        )

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
        while (
            pyautogui.locateCenterOnScreen(
                image=constants.QUEST_COMPLETE_SCREEN,
                confidence=constants.CONFIDENCE,
            )
            != None
            or pyautogui.locateCenterOnScreen(
                image=constants.REPLAY_QUEST,
                confidence=constants.CONFIDENCE,
            )
            != None
        ):
            on_run_complete()

            if pyautogui.locateCenterOnScreen(
                image=constants.CONTINUE_PLAYING_QUEST, confidence=constants.CONFIDENCE
            ):
                Macros.continue_playing()
            Macros.left_click()

        # When the user is requires a revive
        while (
            pyautogui.locateCenterOnScreen(
                image=constants.HP_ZERO, confidence=constants.CONFIDENCE
            )
            != None
        ):
            Macros.left_click_spam()

        time.sleep(1)


if __name__ == "__main__":
    main()
