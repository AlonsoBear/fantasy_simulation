from settings import MAX_COLS, MAX_ROWS, FISH, MANZANAS, ARBOL_DE_MANZANA, GRASS
from random import randint, uniform
import curses
def charToColor(prev):
    if prev == 'Y':
         return 1
    elif prev == 'g':
        return 3
    elif prev == 'w':
        return 2
    elif prev == '.' or prev == 'T':
        return MANZANAS
    elif prev == '©':
        return 4
    elif prev == '>':
        return FISH
    return 1
class Animal():
    def __init__(self, pad):
        # self.x = randint(0,MAX_COLS - 1)
        # self.y = randint(0,MAX_ROWS - 1)
        self.x = 30
        self.y = 25
        attrs = pad.inch(self.x, self.y)
        self.previous = chr(attrs & 0xFF)
        self.hp = 500
        self.hunger = 10
        self.sex_drive = 10
        self.strength = 1
        self.food_radius = 3
        self.mating_radius = 20
        self.sex = "f" if(randint(0,1)) else "m"
        self.character = "O"
        self.pad = pad
        self.pad.addstr(self.x, self.y, self.character)

    def move(self, x, y):
        previus = chr(self.pad.inch(x, y) & 0xFF)
        self.pad.addstr(x, y, self.character)
        self.pad.addstr(self.x, self.y, self.previous, curses.color_pair(charToColor(self.previous)))
        self.x = x
        self.y = y
        self.previous = previus

    def move_to(self):
        #checar su rango de comida
        for look_x in range(self.x - self.food_radius, self.x + self.food_radius ):
            for look_y in range(self.y - self.food_radius, self.y + self.food_radius):
                loking_at = chr(pad.inch(look_x, look_y) & 0xFF)
                if loking_at == '.' or loking_at == 'T' or loking_at == '>':
                    
        new_x = self.x + randint(-1, 1)
        new_y = self.y + randint(-1, 1)
        if(new_x > 499 or new_x < 1 or new_y > 499 or new_x < 1):
            return self.x, self.y
        return new_x, new_y
    
    def cycle(self):
        if(self.is_dead()):
            return
        new_x = self.x + randint(-1, 1)
        new_y = self.y + randint(-1, 1)

        if new_x > 499:
            new_x = 499
        if new_y > 499:
            new_y = 499
        if new_x < 1:
            new_x = 1
        if new_y < 1:
            new_y = 1
        
        if(new_x != self.x or new_y != self.y): self.move(new_x,new_y)

    def is_dead(self):
        self.hp -= 1
        if(self.hp <= 0):
            self.pad.addstr(self.x, self.y, self.previous)
            return True
        return False
    

