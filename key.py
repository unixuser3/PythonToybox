import time
import pyn

def press_keys():
    keyboard = pynput.keyboard.Controller()

    time.sleep(6)  # Wait for 6 seconds

    for key in "qwertyuiopasdfghjklzxcvbnm":
        keyboard.press(key)
        keyboard.release(key)

if __name__ == "__main__":
    press_keys()
