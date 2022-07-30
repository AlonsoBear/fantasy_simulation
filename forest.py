import curses
from curses import wrapper
from random import randint
import time

def gen_forest():

    sizeMap = {
        1: 15,
        2: 27,
        3: 40
    }
    
    seed_column = randint(1, 459)
    seed_row = randint(1, 459)

    forest_column_size = sizeMap[randint(1, 3)]
    forest_row_size = sizeMap[randint(1, 3)]

    for columns in range(seed_column + forest_column_size):
        for Rows in range(seed_row + forest_row_size):
            if randint(1, 3) != 1:
                pass
                pad.addstr(Rows, columns, 'T')

gen_forest()