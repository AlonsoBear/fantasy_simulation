from random import randint

def gen_water(pad, amount):
    for i in range(0, amount):
        sizeMap = {
            1: 10,
            2: 20,
            3: 35
        }
        
        seed_column = randint(1, 459)
        seed_row = randint(1, 459)

        water_column_size = sizeMap[randint(1, 3)]
        water_row_size = sizeMap[randint(1, 3)]

        for columns in range(seed_column, seed_column + water_column_size):
            for Rows in range(seed_row, seed_row + water_row_size):
                pad.addstr(Rows, columns, 'W')




    