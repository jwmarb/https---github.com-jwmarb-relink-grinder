import multiprocessing
import time
import keyboard
from macros import Macros
from utils import (
    battle_results_shown,
    get_timestamp,
    is_hp_zero,
    is_link_attack_available,
    is_sba_gauge_full,
    should_repeat_quest,
    should_replay_quest,
    check_granblue_relink,
)
from utils import format_int
import vgamepad

PROCESS_NOT_BUSY = 0x1
PROCESS_BUSY = 0x7
END_PROCESS = 0x3
PROCESS_TASK_SBA = 0x4
PROCESS_TASK_LINK_ATK = 0x5
PROCESS_TASK_BATTLE_RESULTS = 0x6
runs = 0


class Character:
    LANCELOT = 1
    OTHER = 2

    @Macros.macro
    def lancelot():
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        Macros._gamepad.left_trigger(255)
        Macros._gamepad.update()
        time.sleep(0.01)
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        Macros._gamepad.left_trigger(0)
        Macros._gamepad.update()
        time.sleep(0.01)


def on_run_complete(time_start: float):
    """
    Does stuff when a run has been completed
    """
    global runs
    runs += 1
    log(time_start, f"Runs Completed: {runs}", True)


def battle_results_process(time_start: float, status):
    """
    Detects and handles events relating to battle results screen (the end of a
    quest)
    """

    while status.value is not END_PROCESS:
        has_looped = False
        if battle_results_shown():
            with status.get_lock():
                status.value = PROCESS_BUSY
                while battle_results_shown():
                    if not has_looped:
                        on_run_complete(time_start)
                        has_looped = True
                    # Select replay option first
                    if should_replay_quest():
                        Macros.continue_playing()
                    elif should_repeat_quest():
                        Macros.repeat_quest()
                    else:
                        Macros.xbox_a()
            status.value = PROCESS_NOT_BUSY


def link_attack_process(status):
    """
    Detects and handles link attacks
    """
    while status.value is not END_PROCESS:
        # When a Link Attack is prompted, the player should activate it
        if is_link_attack_available():
            with status.get_lock():
                status.value = PROCESS_BUSY
                Macros.xbox_b()
                while is_link_attack_available():
                    Macros.xbox_b()
            status.value = PROCESS_NOT_BUSY


def sba_process(status):
    """
    Detects and handles SBAs
    """
    while status.value is not END_PROCESS:
        if is_sba_gauge_full():
            with status.get_lock():
                status.value = PROCESS_BUSY
                Macros.use_sba()
                while is_sba_gauge_full():
                    Macros.use_sba()
            status.value = PROCESS_NOT_BUSY


def player_reviver_process(status, character: int):
    """
    Detects and handles when the player is downed
    """

    def revive():
        if character == Character.LANCELOT:
            Macros._gamepad.press_button(
                vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
            )
            Macros._gamepad.update()
            time.sleep(0.5)
            Macros._gamepad.release_button(
                vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
            )
            Macros._gamepad.update()
        else:
            Macros.xbox_a()

    while status.value is not END_PROCESS:
        # When the user is requires a revive
        if is_hp_zero():
            with status.get_lock():
                status.value = PROCESS_BUSY
                revive()
                while is_hp_zero():
                    revive()
            status.value = PROCESS_NOT_BUSY


def log(time_start: float, msg: str, important: bool = False):
    seconds, minutes, hours = get_timestamp(time_start)
    f_seconds = format_int(seconds)
    f_minutes = format_int(minutes)
    f_hours = format_int(hours)
    timestamp = f"{f_hours}:{f_minutes}:{f_seconds}"
    print(f"[{timestamp}]\t" + ("::" if not important else "") + msg)


def terminate_program(start_time: float, status):
    seconds, minutes, hours = get_timestamp(start_time)
    print(f"AFK farm session lasted for {hours}h {minutes}m {seconds}s")
    status.value = END_PROCESS


def main():
    # main constants
    check_granblue_relink()
    print("Type which character you're using")
    print("1. Lancelot (Flight over Fight)")
    print("2. Other (Defensive build)")
    character = int(input())
    time_start = time.perf_counter()

    status = multiprocessing.Value("B", PROCESS_NOT_BUSY)
    p1 = multiprocessing.Process(
        target=battle_results_process, args=(time_start, status)
    )
    p2 = multiprocessing.Process(target=link_attack_process, args=(status,))
    p3 = multiprocessing.Process(target=sba_process, args=(status,))
    keyboard.on_press_key(
        key="esc",
        callback=lambda _: terminate_program(time_start, status),
        suppress=True,
    )
    p4 = multiprocessing.Process(
        target=player_reviver_process, args=(status, character)
    )
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    while status.value is not END_PROCESS:
        match character:
            case Character.LANCELOT:
                if status.value is PROCESS_NOT_BUSY:
                    Character.lancelot()
            case Character.OTHER:
                pass
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # while True:
    #     @decorators.loop_run_once
    #     def on_run_complete():
    #         """
    #         Does stuff when a run has been completed
    #         """
    #         global runs
    #         runs += 1
    #         log(time_start, f"Runs Completed: {runs}", True)

    #     while battle_results_shown():
    #         on_run_complete()
    #         # Select replay option first
    #         if should_replay_quest():
    #             Macros.continue_playing()
    #         elif should_repeat_quest():
    #             Macros.repeat_quest()
    #         else:
    #             Macros.xbox_a()

    #     # When the user is requires a revive
    #     while is_hp_zero():
    #         if character == Character.LANCELOT:
    #             Macros._gamepad.press_button(
    #                 vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    #             )
    #             Macros._gamepad.update()
    #             time.sleep(0.5)
    #             Macros._gamepad.release_button(
    #                 vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    #             )
    #             Macros._gamepad.update()
    #         else:
    #             Macros.xbox_a()

    #     # When a Link Attack is prompted, the player should activate it
    #     while is_link_attack_available():
    #         Macros.xbox_b()

    #     while is_sba_gauge_full():
    #         Macros.use_sba()

    #     match character:
    #         case Character.LANCELOT:
    #             Character.lancelot()
    #         case Character.OTHER:
    #             pass


if __name__ == "__main__":
    main()
