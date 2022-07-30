from random import randint
import curses


def gen_water(pad, amount):
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    WATER = curses.color_pair(2)

    for i in range(0, amount):
        sizeMap = {
            1: 10,
            2: 15,
            3: 30
        }
        
        seed_column = randint(1, 459)
        seed_row = randint(1, 459)

        water_column_size = sizeMap[randint(1, 3)]
        water_row_size = round(sizeMap[randint(1, 3)]/2)

        for columns in range(seed_column, seed_column + water_column_size):
            for rows in range(seed_row, seed_row + water_row_size):
                pad.addstr(rows, columns, ' ', WATER )
