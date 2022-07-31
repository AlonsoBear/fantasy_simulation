from settings import MAX_COLS, MAX_ROWS
from random import randint

class Animal():
    def __init__(self, pad):
        self.x = randint(0,MAX_COLS - 1)
        self.y = randint(0,MAX_ROWS - 1)
        attrs = pad.inch(self.x, self.y)
        self.previous = chr(attrs & 0xFF)
        self.hp = 200
        self.hunger = 10
        self.sex_drive = 10
        self.strength = 1
        self.food_radius = 5
        self.mating_radius = 20
        self.sex = "f" if(randint(0,1)) else "m"
        self.character = "◉"
        self.pad = pad
        self.pad.addstr(self.x, self.y, self.character)

    def move(self, x, y):
        previus = chr(self.pad.inch(x, y) & 0xFF)
        self.pad.addstr(x, y, self.character)
        self.pad.addstr(self.x, self.y, self.previous)
        self.x = x
        self.y = y
        self.previous = previus
    
    def activate(self):
        new_x = self.x + randint(-1,1)
        new_y = self.y + randint(-1,1)

        if new_x > 499:
            new_x = 499
        if new_y > 499:
            new_y = 499
        if new_x < 1:
            new_x = 1
        if new_y < 1:
            new_y = 1
        
        
        self.move(new_x,new_y)

    

