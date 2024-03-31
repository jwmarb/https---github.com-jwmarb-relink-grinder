import enum
import time
import keyboard
import os
from macros import Macros
from utils import (
    can_trade_sigils,
    can_trade_wrightstones,
    has_insufficient_knickknacks,
    has_interactable_checkboxes,
    is_transmute_sigils_screen_shown,
    trade_invoice_shown,
)

DELAY = 0.25


class KnickknackVoucherMethod(enum.Enum):
    TRADE_SIGILS = 1
    TRADE_WRIGHTSTONES = 2
    DO_NOTHING = 3


def exit_listener(_):
    os.system("cls")
    print("Stopped auto-transmute sigils")
    os._exit(0)


def sell_sigils():
    # User navigates back to transmute sigils screen
    while not is_transmute_sigils_screen_shown():
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

    if not can_trade_sigils():
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


def sell_wrightstones():
    # User navigates back to transmute sigils screen
    while not is_transmute_sigils_screen_shown():
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
    while can_trade_wrightstones() and has_interactable_checkboxes():  #
        Macros.xbox_a()
        Macros.xbox_dpad_down()
        time.sleep(0.01)

    time.sleep(DELAY)

    # Trade Wrightstones
    Macros.xbox_x()
    time.sleep(1)

    if not trade_invoice_shown():
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

    print("To pause transmutation, press BACKSPACE")
    print("NOTE: Only works while transmuting sigils")

    def pause_listener(_):
        nonlocal paused
        paused = not paused
        if paused:
            os.system("cls")
            print("Auto-Transmute Sigils Paused")
        else:
            os.system("cls")
            print("To pause transmutation, press BACKSPACE")
            print("NOTE: Only works while transmuting sigils")

    keyboard.on_press_key(
        callback=pause_listener, key="backspace", suppress=True
    )

    keyboard.on_press_key(callback=exit_listener, key="escape", suppress=True)

    while True:
        while not has_insufficient_knickknacks():
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
