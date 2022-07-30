import curses, time 
from curses import wrapper
from random import randint

#local imports
from controllers import controller
from forest import gen_forest

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
    forest_num = randint(10,30)
    
    gen_forest(pad)

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
            
    stdscrn.getch()

wrapper(main)
