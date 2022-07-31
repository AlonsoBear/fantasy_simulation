from settings import MAX_COLS, MAX_ROWS
from random import randint

class Animal():
    def __init__(self, pad):
        self.x = randint(MAX_COLS - 1)
        self.y = randint(MAX_ROWS - 1)
        self.previous = pad.inch(self.x, self.y)
        self.hp = 200
        self.hunger = 10
        self.sex_drive = 10
        self.strength = 1
        self.food_radius = 5
        self.mating_radius = 20
        self.sex = "f" if(randint(0,1)) else "m"
        self.character = "◉"

    def move(self, x, y):
        self.pad.addstr(x, y, self.character)

    

