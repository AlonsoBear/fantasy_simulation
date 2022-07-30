import curses
from curses import wrapper
from random import randint
from controllers import controller

MAX_COLS = 500
MAX_ROWS = 500

def main(stdscrn):
    # stdscrn.clear()
    # stdscrn.refresh()
    # stdscrn.addstr(90, 90, "hello world")
    # time.sleep(100000)
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_ROWS, MAX_COLS)
    stdscrn.nodelay(True)
    stdscrn.clear()
    stdscrn.refresh()

    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            char = chr(randint(65, 65+25))
            pad.addstr(char)

    pad.refresh(0, 0, 0, 0, rows-1, cols-1)

    x, y = 0, 0

    while True:
        clock = 0
        if(clock > 100):
            clock = 0

        x, y = controller(x, y, rows, cols, stdscrn, pad)

        if(clock%50 == 0):
            pass
        clock += 1
             


    # for i in range(50):
    #     pad.refresh(i, 0, 0, 0, rows-1, cols-1)
    #     time.sleep(0.2)
    #     stdscrn.clear()
    #     stdscrn.refresh()
    stdscrn.getch()

wrapper(main)
