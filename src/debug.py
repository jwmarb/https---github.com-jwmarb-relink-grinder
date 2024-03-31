import keyboard
import pyautogui
import constants

if __name__ == "__main__":
    while not keyboard.is_pressed("esc"):
        if keyboard.is_pressed("shift"):
            try:
                print(
                    list(
                        pyautogui.locateAllOnScreen(
                            constants.TRADE_ALL, confidence=0.9
                        )
                    )[0],
                    end="\r",
                )
            except pyautogui.ImageNotFoundException:
                print("", end="\r")
        if keyboard.is_pressed("ctrl"):
            print(pyautogui.position(), end="\r")
