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
from entities.animal import Animal
from tiles import init_tiles

def main(stdscrn):
    logging.basicConfig(filename='../error.log', encoding='utf-8', level=logging.DEBUG)
    rows, cols = stdscrn.getmaxyx()
    pad = curses.newpad(MAX_ROWS, MAX_COLS)
    stdscrn.nodelay(True)
    stdscrn.clear()
    stdscrn.refresh()

    #init tiles intances
    grass, tree, peces, manzanas, arbol_de_manzana, stone, water = init_tiles(pad)
    
    for i in range(MAX_COLS - 1):
        for j in range(MAX_ROWS - 1):
            grass.place(i,j)

    gen_sporadic_trees(tree)

    gen_forest(tree, 300)
    gen_water(water, 100)
    gen_stones(stone, 600)

    gen_food(pad, manzanas,arbol_de_manzana, peces , 20)

    animals = [Animal(pad) for i in range(0, POPULATION)]

    pad.refresh(0, 0, 0, 0, rows-1, cols-1)

    x, y = 0, 0

    clock = 0
    while True:
        if(clock > 1000):
            [animal.cycle() for animal in animals]
            clock = 0

        x, y, escaped = controller(x, y, rows, cols, stdscrn, pad)
        if(escaped):
            break

        clock += 1
            
    stdscrn.getch()

wrapper(main)
