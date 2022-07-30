import curses
from curses import wrapper
from random import randint
import time

MAX_COLS = 500
MAX_ROWS = 500

def main(stdscrn):
    # stdscrn.clear()
    # stdscrn.refresh()
    # stdscrn.addstr(90, 90, "hello world")
    # time.sleep(100000)
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_COLS, MAX_ROWS)
    stdscrn.refresh()
    stdscrn.addstr(10, 10, f"{rows},{cols}")

    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            char = chr(randint(65, 65+25))
            pad.addstr(char)

    for i in range(50):
        pad.refresh(0, 0, i, 0, rows-1, cols-1)
        time.sleep(0.2)
        stdscrn.clear()
        stdscrn.refresh()
    stdscrn.getch()

wrapper(main)
