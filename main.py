from helpers.click_listener import ClickBinder
from pynput.mouse import Button
import pyautogui as pg
import time

def main():
    click_binder = ClickBinder()
    click_binder.bind(Button.x1, lambda: pg.press("left"))
    click_binder.bind(Button.x2, lambda: pg.press("right"))
    click_binder.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        click_binder.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        click_binder.stop()

if __name__ == "__main__":
    main()
