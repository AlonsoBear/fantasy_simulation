import curses, logging
from curses import wrapper
from random import randint

#local imports
from controllers import controller
from map.forest import gen_forest, gen_sporadic_trees
from map.water import gen_water
from map.stone import gen_stones
from settings import *
from map.food import gen_food
from npcs.animal import Animal

def main(stdscrn):
    logging.basicConfig(filename='../error.log', encoding='utf-8', level=logging.DEBUG)
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_ROWS, MAX_COLS)
    stdscrn.nodelay(True)
    stdscrn.clear()
    stdscrn.refresh()

    curses.init_color(GRASS, 16, 227, 0) # grass
    curses.init_pair(3, GRASS, GRASS)
    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            char = 'g'
            pad.addstr(char, curses.color_pair(3))

    gen_sporadic_trees(pad)

    forest_num = randint(10,30)
    
    gen_forest(pad, 300)
    gen_water(pad, 100)
    gen_stones(pad, 600)

    gen_food(pad)

    animals = [Animal(pad) for i in range(0, POPULATION)]

    pad.refresh(0, 0, 0, 0, rows-1, cols-1)

    x, y = 0, 0

    clock = 0
    while True:
        if(clock > 5000):
            [animal.cycle() for animal in animals]
            clock = 0

        x, y, escaped = controller(x, y, rows, cols, stdscrn, pad)
        if(escaped):
            break

        clock += 1
            
    stdscrn.getch()

wrapper(main)
