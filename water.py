from random import randint

def gen_water(pad):

    sizeMap = {
        1: 10,
        2: 20,
        3: 35
    }
    
    seed_column = randint(1, 459)
    seed_row = randint(1, 459)

    water_column_size = sizeMap[randint(1, 3)]
    water_row_size = sizeMap[randint(1, 3)]

    


    