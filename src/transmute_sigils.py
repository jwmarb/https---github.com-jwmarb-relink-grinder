import constants
import keyboard
import threading
import os
from macros import Macros
from utils import is_on_screen

def exit_listener():
    while not keyboard.is_pressed("escape"):
        pass
    os._exit(0)

def main():
    paused = False

    def pause_listener(_):
        nonlocal paused
        paused = not paused
        print("Auto-Transmute Sigils Paused" if paused else "Resumed Auto-Transmute Sigils")

    keyboard.on_press_key(callback=pause_listener, key="backspace", suppress=True)

    keyboard.on_press_key(callback=exit_listener, key="escape", suppress=True)

    threading.Thread(target=exit_listener).start()
    
    while not is_on_screen(constants.INSUFFICIENT_KNICKKNACKS):
        if not paused:
            Macros.left_click()

if __name__ == '__main__':
    main()