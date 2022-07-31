import curses
from curses import wrapper
from random import randint
import logging

def gen_food(pad):
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    
    
    for columns in range(20):
        for Rows in range(20):
            if randint(1, 10) == 1:
                attrs = pad.inch(Rows, columns)
                current_value = chr(attrs & 0xFF)

                if current_value == 'w':
                    pad.addstr(Rows, columns, 'F')
                elif current_value == 'g':
                    pad.addstr(Rows, columns, 'M')
                elif current_value == 'T':
                    pad.addstr(Rows, columns, 'P')
                
                