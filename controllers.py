from settings import MAX_COLS, MAX_ROWS

def controller(x, y, rows, cols, stdscr, pad):
    escaped = False
    try:
        key = stdscr.getkey()
    except:
        key = None

    if (key == 'KEY_UP' and y > 0):
        y -= 1
    elif (key == 'KEY_DOWN' and y <= MAX_ROWS - rows - 3):
        y += 1
    elif (key == 'KEY_LEFT' and x > 0):
        x -= 1
    elif (key == 'KEY_RIGHT' and x <= MAX_COLS - cols):
        x += 1
    elif (key == "Q"):
        escaped = True

    if(key != None):
        stdscr.clear()
    pad.refresh(y, x, 0, 0, rows-1, cols-1)
    stdscr.refresh()

    return x, y, escaped