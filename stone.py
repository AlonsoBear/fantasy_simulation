from random import randint
import curses

def gen_stones(pad, amount):
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
                pad.addstr(rows, columns, 'O')



