import os
import time


def clear_screen(seconds=None):
    if isinstance(seconds, (int, float)):
        time.sleep(seconds)
        os.system("cls" if os.name == "nt" else "clear")
    elif seconds is None:
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\033[31mInvalid input for clear_screen\033[0m")


def hide_cursor():
    print("\033[?25l")


def show_cursor():
    print("\033[?25h")
