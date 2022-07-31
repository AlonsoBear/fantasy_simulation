from random import randint
import curses


def gen_water(water, amount):
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
                water.place(columns,rows)
