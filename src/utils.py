import os
import time

import pyautogui
import constants
import win32gui


def get_timestamp(
    start_time: float = time.perf_counter(),
) -> tuple[int, int, int]:
    now = max(int(time.perf_counter() - start_time), 0)
    seconds = now % 60
    minutes = (now // 60) % 60
    hours = (now // 3600) % 24
    return (seconds, minutes, hours)


def terminate_program(start_time: float):
    seconds, minutes, hours = get_timestamp(start_time)
    print(f"AFK farm session lasted for {hours}h {minutes}m {seconds}s")
    os._exit(0)


def check_granblue_relink():
    hwnd = win32gui.FindWindow(None, constants.HWND_NAME)
    if hwnd == 0:
        err = "Granblue Fantasy: Relink must be running to execute this script"
        print(err)
        os._exit(0)


def format_int(n: int) -> str:
    if n >= 10:
        return str(n)

    return "0" + str(n)


def is_on_screen(*images: str, c: float = constants.CONFIDENCE):
    for file in images:
        try:
            pyautogui.locateOnScreen(image=file, confidence=c)
            return True
        except pyautogui.ImageNotFoundException:
            pass

    return False
