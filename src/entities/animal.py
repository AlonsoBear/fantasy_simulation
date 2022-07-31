from settings import MAX_COLS, MAX_ROWS, FISH, MANZANAS, ANIMALS
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
    
    # INITIALIZATION METHODS
    def __init__(self, pad):
        self.x = randint(0,MAX_COLS - 1)
        self.y = randint(0,MAX_ROWS - 1)
        attrs = pad.inch(self.x, self.y)
        self.previous = chr(attrs & 0xFF)
        self.hp = 500
        self.hunger = 10
        self.sex_drive = 10
        self.strength = 1
        self.scan_radius = 5
        self.sex = "f" if(randint(0,1)) else "m"
        self.character = "O"
        self.pad = pad
        self.near_food = []
        self.near_mates = []

    def born(self):
        self.pad.addstr(self.x, self.y, self.character)
        self.first_scan()

    def first_scan(self):
        for look_x in range(self.x - self.scan_radius, self.x + self.scan_radius):
            for look_y in range(self.y - self.scan_radius, self.y + self.scan_radius):
                looking_at = chr(self.pad.inch(look_x, look_y) & 0xFF)
                if looking_at == '.' or looking_at == 'T' or looking_at == '>':
                    pass # SAVE FOOD
                elif looking_at == 'O':
                    self.near_mates = [ANIMALS.push(animal) for animal in ANIMALS if(animal.x == look_x and animal.y == look_y)]

    # ACTION METHODS
    def move(self, x, y):
        previus = chr(self.pad.inch(x, y) & 0xFF)
        self.pad.addstr(x, y, self.character)
        self.pad.addstr(self.x, self.y, self.previous, curses.color_pair(charToColor(self.previous)))
        self.x = x
        self.y = y
        self.previous = previus
    
    def look_for_food(self):
        pass

    def move_to(self):
        if(self.is_hungry()):
            new_x, new_y = self.look_for_food()
        elif(self.is_horny() and len(self.near_mates) > 0):
            new_x, new_y = self.look_for_mate()
        else:
            new_x, new_y = self.x + randint(-1, 1), self.y + randint(-1, 1)
            
        value_in_new_location = chr(self.pad.inch(new_x, new_y) & 0xFF)
        if(new_x > 499 or new_x < 1 or new_y > 499 or new_y < 1 or value_in_new_location == "O"):
            return self.x, self.y
        return new_x, new_y

    def eat(self,new_x, new_y, loking_at):
        if loking_at == '.': self.pad.addstr(new_x, new_y, 'g', curses.color_pair(3))
        elif loking_at == 'T': self.pad.addstr(new_x, new_y, 'Y', curses.color_pair(1))
        elif loking_at == '>': self.pad.addstr(new_x, new_y, 'w', curses.color_pair(2))
    
    def cycle(self):
        if(self.is_dead()): return
        new_x, new_y = self.move_to()
        if(new_x != self.x or new_y != self.y): self.move(new_x,new_y)

    def look_for_mate(self):
        mate = self.near_mates.pop()
        return mate.x, mate.y


    # STATE METHODS
    def is_dead(self):
        # self.hp -= 1
        if(self.hp <= 0):
            self.pad.addstr(self.x, self.y, self.previous)
            return True
        return False
    
    def is_horny(self):
        self.sex_drive -= 1
        if (self.sex_drive <= 0):
            return True
        return False

    def is_hungry(self):
        self.hunger -= 1
        if (self.hunger <= 5):
            if(self.hunter <= 0):
                self.hp -= 1
            return True
        return False

    # STATIC METHODS
    @staticmethod
    def mate(self, lover_a, lover_b):
        lover_a.sex_drive = 10
        lover_b.sex_drive = 10

        if(randint(0, 1)): 
            return Animal(self.pad)
        return None
        
