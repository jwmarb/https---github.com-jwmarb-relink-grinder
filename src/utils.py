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


def is_on_screen(
    *images: str,
    c: float = constants.CONFIDENCE,
    region: tuple[int, int, int, int],
):
    for file in images:
        try:
            pyautogui.locateOnScreen(image=file, confidence=c, region=region)
            return True
        except pyautogui.ImageNotFoundException:
            pass

    return False


def is_sba_gauge_full():
    try:
        pyautogui.locateOnScreen(
            constants.SBA_GAUGE_FULL,
            region=(899, 700, 120, 200),
            confidence=0.4,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def is_link_attack_available():
    try:
        pyautogui.locateOnScreen(
            constants.LINK_ATTACK,
            region=(1130, 650, 180, 50),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def is_hp_zero():
    try:
        pyautogui.locateOnScreen(
            constants.HP_ZERO,
            region=(533, 680, 166, 27),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def battle_results_shown():
    try:
        pyautogui.locateOnScreen(
            constants.REPLAY_QUEST, region=(689, 490, 540, 36), confidence=0.5
        )
        return True
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.locateOnScreen(
                constants.QUEST_COMPLETE_SCREEN,
                region=(108, 41, 722, 67),
                confidence=0.5,
            )
            return True
        except pyautogui.ImageNotFoundException:
            return False


def should_repeat_quest():
    try:
        pyautogui.locateOnScreen(
            constants.REPEAT_QUEST_FIRST_PROMPT,
            region=(229, 950, 104, 40),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def should_replay_quest():
    try:
        pyautogui.locateOnScreen(
            constants.CONTINUE_PLAYING_QUEST,
            region=(780, 460, 358, 60),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def is_transmute_sigils_screen_shown():
    try:
        pyautogui.locateOnScreen(
            constants.SELECT_TRANSMUTATION,
            region=(59, 179, 597, 244),
            confidence=0.95,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def has_insufficient_knickknacks():
    try:
        pyautogui.locateOnScreen(
            constants.INSUFFICIENT_KNICKKNACKS,
            region=(766, 730, 386, 25),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def can_trade_sigils():
    try:
        pyautogui.locateOnScreen(
            constants.TRADE_ALL,
            region=(723, 591, 132, 169),
            confidence=constants.CONFIDENCE,
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False


def has_interactable_checkboxes():
    try:
        pyautogui.locateOnScreen(
            constants.WRIGHTSTONES_BLANKCHECKBOX, confidence=0.98
        )

        return True
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.locateOnScreen(
                constants.WRIGHTSTONES_BLANKCHECKBOX_SELECTED, confidence=0.98
            )
            return True
        except pyautogui.ImageNotFoundException:
            return False


def can_trade_wrightstones():
    try:
        pyautogui.locateOnScreen(
            constants.WRIGHTSTONES_EXCESSIVE,
            confidence=constants.CONFIDENCE,
            region=(607, 492, 719, 91),
        )
        pyautogui.locateOnScreen(
            constants.WRIGHTSTONES_UNABLE_TO_SELECT,
            confidence=constants.CONFIDENCE,
            region=(775, 504, 354, 72),
        )
        return False
    except pyautogui.ImageNotFoundException:
        return True


def trade_invoice_shown():
    try:
        pyautogui.locateOnScreen(
            constants.TRADE_INVOICES,
            confidence=constants.CONFIDENCE,
            region=(830, 88, 267, 226),
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False
