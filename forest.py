import curses
from curses import wrapper
from random import randint
from settings import GRASS, TREE
from utils import rgb

def gen_forest(pad, amount):

    sizeMap = {
        1: 15,
        2: 27,
        3: 40
    }

    curses.init_color(GRASS, rgb(17), rgb(130), rgb(0)) # grass
    curses.init_color(TREE, 11,   37,   10) # tree
    curses.init_pair(1, TREE, GRASS)
    COLOR_ARBOLES = curses.color_pair(1)

    for k in range(amount):
        seed_column = randint(1, 459)
        seed_row = randint(1, 459)

        forest_column_size = sizeMap[randint(1, 3)]
        forest_row_size = sizeMap[randint(1, 3)]

        for columns in range(seed_column, seed_column + forest_column_size):
            for Rows in range(seed_row, seed_row + forest_row_size):
                if randint(1, 6) == 1:
                    pad.addstr(Rows, columns, '⍋', COLOR_ARBOLES)