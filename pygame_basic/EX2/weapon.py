from Character import *

class weapon(Character) :
    def __init__(self):
        self.character_speed = - 10
        self.character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX2/Spear.png')
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
    def setXY(self, x, y) :
        self.character_x = x
        self.character_y = y

    def move(self) :
        self.character_y += self.character_speed
