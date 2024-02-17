import os
import time
from typing import Callable
import win32gui
from cancelable_thread import CancelableThread
import constants
import keyboard
import win32api


class Macros:
    _relink_hwnd: int | None = None
    _cur_hwnd: int | None = None
    _cur_pos: tuple[int, int] | None = None
    _thread: CancelableThread | None = None
    _is_executing: bool = False

    @staticmethod
    def _get_relink_hwnd():
        """
        Gets the relink hwnd
        """
        if Macros._relink_hwnd == None:
            Macros._relink_hwnd = win32gui.FindWindow(None, constants.HWND_NAME)
            if Macros._relink_hwnd == 0:
                raise Exception('"Granblue Fantasy: Relink" not detected')
        return Macros._relink_hwnd

    @staticmethod
    def _cur_hwnd_handler():
        """
        Handles the current hwnd
        """
        if Macros._cur_hwnd == None:
            Macros._cur_hwnd = win32gui.GetForegroundWindow()
            if Macros._cur_hwnd != Macros._get_relink_hwnd():
                Macros._cur_pos = win32api.GetCursorPos()
                Macros._thread = CancelableThread(
                    lambda is_stopped: Macros._reset_cur_hwnd(is_stopped)
                )
                Macros._thread.start()
        elif Macros._cur_hwnd != Macros._get_relink_hwnd():
            Macros._thread.stop()
            Macros._thread = CancelableThread(
                lambda is_stopped: Macros._reset_cur_hwnd(is_stopped)
            )
            Macros._thread.start()

    @staticmethod
    def _reset_cur_hwnd(is_stopped: Callable[[], bool]):
        if Macros._relink_hwnd == None:
            raise Exception("Tried to reset current hwnd when it is undefined")

        # Wait for main thread to finish executing bin file
        while not is_stopped() and Macros._is_executing:
            pass

        time.sleep(3)

        if not is_stopped() and win32gui.GetForegroundWindow() != Macros._cur_hwnd:
            keyboard.press_and_release("alt")
            win32gui.SetForegroundWindow(Macros._cur_hwnd)
            win32api.SetCursorPos(Macros._cur_pos)
            Macros._cur_hwnd = None

    @staticmethod
    def _exec(file_name: str):
        """
        Executes a macro from the bin folder
        """
        Macros._cur_hwnd_handler()

        # Focuses application window, if applicable
        if win32gui.GetForegroundWindow() != Macros._get_relink_hwnd():
            keyboard.press_and_release("alt")
            win32gui.SetForegroundWindow(Macros._get_relink_hwnd())

        Macros._is_executing = True
        os.system(f"\"{os.path.abspath(os.path.join('bin', file_name))}.exe\"")
        Macros._is_executing = False

    @staticmethod
    def continue_playing():
        """
        Whenever a popup prompts the user to continue playing the quest, it
        will automatically select yes
        """
        Macros._exec("continue_playing")

    @staticmethod
    def left_click():
        """
        Simulates a left click in the application
        """
        Macros._exec("left_click")

    @staticmethod
    def left_click_spam():
        """
        Spams left clicks. Useful for reviving the character
        """
        Macros._exec("left_click_spam")
