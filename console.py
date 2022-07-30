import curses
from curses import wrapper

def main(stdscrn):
    stdscrn.clear()
    rows, cols = stdscrn.getmaxyx()
    stdscrn.addstr(rows,cols,f"{rows} {cols}")
    stdscrn.refresh()
    stdscrn.getch()

window = curses.initscr()
window.resize(45, 200)
wrapper(main)
