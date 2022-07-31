import curses, logging
from curses import wrapper
from random import randint

from utils import rgb

from settings import MAX_COLS, MAX_ROWS
from settings import FISH, MANZANAS, ARBOL_DE_MANZANA, GRASS

def gen_food(pad, manzanas ,arbol_de_manzana, peces, abundance):
    curses.init_color(FISH, rgb(250), rgb(128), rgb(114)) # salmon
    curses.init_pair(FISH, FISH, curses.COLOR_CYAN)
    COLOR_PECES = curses.color_pair(FISH)

    curses.init_color(MANZANAS, rgb(214), rgb(32), rgb(21))
    curses.init_color(GRASS, rgb(17), rgb(130), rgb(0)) # grass
    curses.init_pair(MANZANAS, MANZANAS, GRASS)
    COLOR_MANZANAS = curses.color_pair(MANZANAS)

    for columns in range(MAX_COLS - 1):
        for Rows in range(MAX_ROWS - 1):
            if randint(1, abundance) == 1:
                attrs = pad.inch(Rows, columns)
                current_value = chr(attrs & 0xFF)

                if current_value == 'w':
                    peces.place(columns,Rows)
                elif current_value == 'g':
                    manzanas.place(columns,Rows)
                elif current_value == 'Y':
                    arbol_de_manzana.place(columns,Rows)
                
                