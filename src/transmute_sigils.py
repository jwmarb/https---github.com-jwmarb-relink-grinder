import time
import constants
import keyboard
import threading
import os
from macros import Macros
from utils import is_on_screen


def exit_listener(_):
    os._exit(0)


def main():
    paused = False
    DELAY = 0.25

    def pause_listener(_):
        nonlocal paused
        paused = not paused
        print(
            "Auto-Transmute Sigils Paused"
            if paused
            else "Resumed Auto-Transmute Sigils"
        )

    keyboard.on_press_key(
        callback=pause_listener, key="backspace", suppress=True
    )

    keyboard.on_press_key(callback=exit_listener, key="escape", suppress=True)

    while True:
        while not is_on_screen(constants.INSUFFICIENT_KNICKKNACKS):
            if not paused:
                Macros.xbox_a()

        # User navigates back to transmute sigils screen
        while not is_on_screen(constants.SELECT_TRANSMUTATION, c=0.99):
            Macros.xbox_a()
            time.sleep(0.5)

        time.sleep(1)

        # Back to main navigation
        Macros.xbox_b()
        time.sleep(DELAY)

        # Highlights "Knickknack Vouchers"
        Macros.xbox_dpad_up()
        time.sleep(DELAY)

        # Navigates into "Knickknack Vouchers"
        Macros.xbox_a()
        time.sleep(DELAY)

        # Navigates into "Trade Sigils"
        Macros.xbox_a()
        time.sleep(DELAY)

        # Opens "Sort & Filter/Trade All"
        Macros.xbox_back()
        time.sleep(DELAY)

        # "Trade All Using Specified Criteria"
        Macros.xbox_x()
        time.sleep(1)

        if not is_on_screen(constants.TRADE_ALL):
            print("You have no more sigils to trade for")
            os._exit(0)

        # Moves from "Cancel" to "Trade"
        Macros.xbox_dpad_up()
        time.sleep(DELAY)

        # Navigates to "Trade"
        Macros.xbox_a()
        time.sleep(1)

        # Ticks "Trade" button since the trade includes high rarity Sigils
        Macros.xbox_a()
        time.sleep(DELAY)

        # Navigates to unlocked "Trade" button
        Macros.xbox_dpad_down()
        time.sleep(DELAY)

        # Confirms action
        Macros.xbox_a()
        time.sleep(DELAY)

        # Exits out of "Thank You!"
        Macros.xbox_a()
        time.sleep(0.5)

        # Goes back to Knickknack Vouchers menu
        Macros.xbox_b()
        time.sleep(DELAY)

        # Goes back to Main screen (Siero's Knickknack Shack)
        Macros.xbox_b()
        time.sleep(DELAY)

        # Navigates to "Transmute Sigils"
        Macros.xbox_dpad_down()
        time.sleep(DELAY)

        # Confirms navigation
        Macros.xbox_a()
        time.sleep(DELAY)

        # At this point, the process starts again until the user desires to 
        # end the script



if __name__ == "__main__":
    main()
