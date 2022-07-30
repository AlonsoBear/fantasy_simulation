import curses
from curses import wrapper
from random import randint

#local imports
from controllers import controller
from forest import gen_forest
from water import gen_water
from stone import gen_stones

MAX_COLS = 500
MAX_ROWS = 500

def main(stdscrn):
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_ROWS, MAX_COLS)
    stdscrn.nodelay(True)
    stdscrn.clear()
    stdscrn.refresh()

    curses.init_color(curses.COLOR_YELLOW, 42,   162,   42)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            char = ' '
            pad.addstr(char, curses.color_pair(3))
    forest_num = randint(10,30)
    
    gen_forest(pad, 300)
    gen_water(pad, 100)
    gen_stones(pad, 600)

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
