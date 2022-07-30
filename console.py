import curses
from curses import wrapper
from controllers import controller
from water import gen_water

MAX_COLS = 500
MAX_ROWS = 500

def main(stdscrn):
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_ROWS, MAX_COLS)
    stdscrn.nodelay(True)
    stdscrn.clear()
    stdscrn.refresh()

    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            char = ','
            pad.addstr(char)

    pad.refresh(0, 0, 0, 0, rows-1, cols-1)

    x, y = 0, 0

    while True:
        clock = 0
        if(clock > 100):
            clock = 0

        x, y, escaped = controller(x, y, rows, cols, stdscrn, pad)
        if(escaped):
            break

        if(clock%50 == 0):
            pass
        clock += 1
            
    stdscrn.getch()

wrapper(main)
