import time
from typing import Callable
import pyautogui
import win32gui
import constants
import vgamepad


class Macros:
    _relink_hwnd: int | None = None
    _gamepad = vgamepad.VX360Gamepad()

    @staticmethod
    def _find_window(name: str):
        return win32gui.FindWindow(None, name)

    @staticmethod
    def _get_relink_hwnd():
        """
        Gets the relink hwnd
        """
        if Macros._relink_hwnd is None:
            Macros._relink_hwnd = Macros._find_window(constants.HWND_NAME)
            if Macros._relink_hwnd == 0:
                raise Exception('"Granblue Fantasy: Relink" not detected')
        return Macros._relink_hwnd

    @staticmethod
    def macro(fn: Callable[[], None]):
        """
        Executes a macro based on virtual gamepad
        """

        def wrapper():
            # Focuses application window, if applicable
            if win32gui.GetForegroundWindow() != Macros._get_relink_hwnd():
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(Macros._get_relink_hwnd())

            fn()

        return wrapper

    @staticmethod
    def delay():
        """
        Forces the thread to sleep so that there is a delay
        """
        time.sleep(constants.INPUT_DELAY)

    @staticmethod
    @macro
    def continue_playing():
        """
        Whenever a popup prompts the user to continue playing the quest, it
        will automatically select yes
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
        )
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def left_click():
        """
        Simulates a left click in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def repeat_quest():
        """
        Turns on Repeat Quest during the battle results screen
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()
