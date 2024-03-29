import enum
import time
import constants
import keyboard
import os
from macros import Macros
from utils import is_on_screen

DELAY = 0.25


class KnickknackVoucherMethod(enum.Enum):
    TRADE_SIGILS = 1
    TRADE_WRIGHTSTONES = 2
    DO_NOTHING = 3


def exit_listener(_):
    os.system('cls')
    print("Stopped auto-transmute sigils")
    os._exit(0)


def sell_sigils():
    # User navigates back to transmute sigils screen
    while not is_on_screen(constants.SELECT_TRANSMUTATION, c=0.99):
        Macros.xbox_a()
        time.sleep(0.5)

    time.sleep(DELAY)

    # Back to main navigation
    Macros.xbox_b()
    time.sleep(1)

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


SHOULD_STOP_WRIGHTSTONE_TRADE = [
    constants.WRIGHTSTONES_EXCESSIVE,
    constants.WRIGHTSTONES_UNABLE_TO_SELECT,
]


def sell_wrightstones():
    # User navigates back to transmute sigils screen
    while not is_on_screen(constants.SELECT_TRANSMUTATION, c=0.99):
        Macros.xbox_a()
        time.sleep(0.5)

    time.sleep(1)

    # Back to main navigation
    Macros.xbox_b()
    time.sleep(DELAY * 3)

    # Highlights "Knickknack Vouchers"
    Macros.xbox_dpad_up()
    time.sleep(DELAY)

    # Navigates into "Knickknack Vouchers"
    Macros.xbox_a()
    time.sleep(DELAY)

    # Navigates into "Trade Wrightstones"
    Macros.xbox_a()
    time.sleep(DELAY)

    # Selects as many wrightstones as it can
    while not is_on_screen(*SHOULD_STOP_WRIGHTSTONE_TRADE):
        Macros.xbox_a()
        Macros.xbox_dpad_down()
        time.sleep(0.01)
        if not is_on_screen(constants.WRIGHTSTONES_BLANKCHECKBOX, c=0.9) or \
        not is_on_screen(constants.WRIGHTSTONES_BLANKCHECKBOX_SELECTED, c=0.9):
            break

    time.sleep(DELAY)

    # Trade Wrightstones
    Macros.xbox_x()
    time.sleep(1)

    if not is_on_screen(constants.TRADE_INVOICES):
        print("You have no more wrightstones to trade for")
        os._exit(0)

    # Moves from Cancel to Trade
    Macros.xbox_dpad_up()
    time.sleep(DELAY)

    # Confirms "Trade"
    Macros.xbox_a()
    time.sleep(DELAY)

    # Ticks Trade
    Macros.xbox_a()
    time.sleep(DELAY)

    # Navigates to "Trade" option
    Macros.xbox_dpad_down()
    time.sleep(DELAY)

    # Confirms "Trade"
    Macros.xbox_a()
    time.sleep(DELAY)

    # Exits out of prompt by preessing "OK"
    Macros.xbox_a()
    time.sleep(DELAY)

    # Exits out of "Trade Wrightstones"
    Macros.xbox_b()
    time.sleep(DELAY)

    # Exits out of "Knickknack Vouchers"
    Macros.xbox_b()
    time.sleep(DELAY)

    # Moves selected option top "Transmute Sigils"
    Macros.xbox_dpad_down()
    time.sleep(DELAY)

    # Confirms navigation into "Transmute Sigils"
    Macros.xbox_a()
    time.sleep(DELAY)


def main():
    paused = False
    option: int | None = None

    while option is None:
        print("Select restock knickknack vouchers method")
        print("1. Trade Sigils")
        print("2. Trade Wrightstones")
        print("3. Do nothing")
        option = int(input("\nType an option (1-3): ").strip())
        os.system("cls")

    print(
        "To pause transmutation, press BACKSPACE"
    )
    print("NOTE: Only works while transmuting sigils")

    def pause_listener(_):
        nonlocal paused
        paused = not paused
        if paused:
            os.system("cls")
            print("Auto-Transmute Sigils Paused")
        else:
            os.system("cls")
            print(
                "To pause transmutation, press BACKSPACE"
            )
            print("NOTE: Only works while transmuting sigils")

    keyboard.on_press_key(
        callback=pause_listener, key="backspace", suppress=True
    )

    keyboard.on_press_key(callback=exit_listener, key="escape", suppress=True)

    while True:
        while not is_on_screen(constants.INSUFFICIENT_KNICKKNACKS):
            if not paused:
                Macros.xbox_a()

        match option:
            case KnickknackVoucherMethod.DO_NOTHING.value:
                continue
            case KnickknackVoucherMethod.TRADE_SIGILS.value:
                sell_sigils()
            case KnickknackVoucherMethod.TRADE_WRIGHTSTONES.value:
                sell_wrightstones()


if __name__ == "__main__":
    main()
