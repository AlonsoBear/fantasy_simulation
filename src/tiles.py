from entities.tile import Tile
import curses
from settings import *
from utils import rgb

def init_tiles(pad):
    curses.init_color(GRASS, 16, 227, 0) # grass
    curses.init_pair(3, GRASS, GRASS)
    curses.init_color(GRASS, rgb(17), rgb(130), rgb(0)) # grass
    curses.init_color(TREE, 11,   37,   10) # tree
    curses.init_pair(1, TREE, GRASS)
    COLOR_ARBOLES = curses.color_pair(1)
    

    curses.init_color(FISH, rgb(250), rgb(128), rgb(114)) # salmon
    curses.init_pair(FISH, FISH, curses.COLOR_CYAN)
    COLOR_PECES = curses.color_pair(FISH)

    curses.init_color(MANZANAS, rgb(214), rgb(32), rgb(21))
    curses.init_color(GRASS, rgb(17), rgb(130), rgb(0)) # grass
    curses.init_pair(MANZANAS, MANZANAS, GRASS)
    COLOR_MANZANAS = curses.color_pair(MANZANAS)

    curses.init_color(STONE, rgb(50), rgb(50), rgb(50))
    curses.init_color(STONE_BG, rgb(105), rgb(105), rgb(105))
    curses.init_pair(4, STONE, STONE_BG)
    STONE_COLOR = curses.color_pair(4)
    

    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_CYAN)
    WATER = curses.color_pair(2)

    arbol_de_manzana = Tile(pad, "A_M", 'T', COLOR_MANZANAS)
    peces = Tile(pad, "pez", '>', COLOR_PECES)
    manzanas = Tile(pad, "manzana", '.', COLOR_MANZANAS)
    tree = Tile(pad, "tree", 'Y', curses.color_pair(1))
    stone = Tile(pad, "piedra", '©', STONE_COLOR)
    water = Tile(pad, "agua", 'w', WATER)
    grass = Tile(pad, "gras", 'g', curses.color_pair(3))
    
    return grass, tree, peces, manzanas, arbol_de_manzana, stone, water