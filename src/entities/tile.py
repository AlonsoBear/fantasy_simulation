class Tile():
    def __init__(self, pad, name, character, color_pair):
        self.pad = pad
        self.name = name
        self.character = character
        self.color_pair = color_pair
    def place(self, x,y):
        self.pad.addstr(y, x,self.character, self.color_pair)