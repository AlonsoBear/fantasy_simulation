from settings import MAX_COLS, MAX_ROWS, FISH, MANZANAS, ARBOL_DE_MANZANA, GRASS
from random import randint, uniform
import curses,logging

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
        #self.x = randint(0,MAX_COLS - 1)
        #self.y = randint(0,MAX_ROWS - 1)
        self.x = 30
        self.y = 25
        attrs = pad.inch(self.x, self.y)
        self.previous = chr(attrs & 0xFF)
        self.hp = 500
        self.hunger = 10
        self.sex_drive = 10
        self.strength = 1
        self.food_radius = 1
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
    
    """ def look_for_food(self):
        found_food = False
        new_x = self.x
        new_y = self.y

        #checar su rango de comida
        for mod_x in range(-1,1)
            for mod_y in range(-1,1)
                loking_at = chr(self.pad.inch(self.x + mod_x, self.y + mod_y) & 0xFF)
                if loking_at == '.' or loking_at == 'T' or loking_at == '>':
                    found_food = True
                    new_x = self.x + mod_x
                    new_y = self.y + mod_y
                    #if they get to the food they should eat it
                    self.eat(new_x, new_y, loking_at)
                    break
                else:
                    continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break
        return new_x, new_y, found_food """
    
    def eat(self,new_x, new_y, loking_at):
        if loking_at == '.': self.pad.addstr(new_x, new_y, 'g', curses.color_pair(3))
        elif loking_at == 'T': self.pad.addstr(new_x, new_y, 'Y', curses.color_pair(1))
        elif loking_at == '>': self.pad.addstr(new_x, new_y, 'w', curses.color_pair(2))
        
    def move_to(self):
        #new_x, new_y, found_food = self.look_for_food()
        if not False:
            new_x = self.x + randint(-1, 1)
            new_y = self.y + randint(-1, 1)
        if(new_x > 499 or new_x < 1 or new_y > 499 or new_y < 1):
            return self.x, self.y
        return new_x, new_y
    
    def cycle(self):
        if(self.is_dead()): return
        #if(self.is_horny()): self.look_for_mate()
        new_x, new_y = self.move_to()

        if(new_x != self.x or new_y != self.y): self.move(new_x,new_y)

    def is_dead(self):
        self.hp -= 1
        if(self.hp <= 0):
            self.pad.addstr(self.x, self.y, self.previous)
            return True
        return False
    
    def is_horny(self):
        self.sex_drive -= 1
        if (self.sex_drive <= 4):
            return True
        return False

    def look_for_mate(self):
        pass

    @staticmethod
    def mate(self, lover_a, lover_b):
        lover_a.sex_drive = 10
        lover_b.sex_drive = 10

        if(randint(0, 1)): 
            return Animal(self.pad)
        return None
        
