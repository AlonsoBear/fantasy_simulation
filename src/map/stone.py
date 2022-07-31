from random import randint
import curses
from settings import STONE, STONE_BG
from utils import rgb

def gen_stones(pad, amount):
    curses.init_color(STONE, rgb(50), rgb(50), rgb(50))
    curses.init_color(STONE_BG, rgb(105), rgb(105), rgb(105))
    curses.init_pair(4, STONE, STONE_BG)
    STONE_COLOR = curses.color_pair(4)

    for i in range(0, amount):
        sizeMap = {
            1: 2,
            2: 4,
            3: 8
        }
        
        seed_column = randint(1, 459)
        seed_row = randint(1, 459)

        stone_column_size = sizeMap[randint(1, 3)]
        stone_row_size = round(sizeMap[randint(1, 3)]/2)

        for columns in range(seed_column, seed_column + stone_column_size):
            for rows in range(seed_row, seed_row + stone_row_size):
                pad.addstr(rows, columns, '©', STONE_COLOR)



