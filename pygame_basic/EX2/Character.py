import pygame

class Character :
    character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX2/penguin.png')
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x = 0
    character_y = 0
    character_speed = 0
    to_x = 0
    character_rect = character.get_rect()
    character_rect.left = character_x
    character_rect.top = character_y

    def __init__(self, speed) :
        self.character_speed = speed
        self.character_x = 640/2 - self.character_width/2
        self.character_y = 480 - self.character_height
    def go_right(self) :
        self.to_x += self.character_speed
    def go_left(self) :
        self.to_x -= self.character_speed
    def set_speed(self, speed) :
        self.character_speed = speed
    def reset_to_x(self) :
        self.to_x = 0
    def get_x(self) :
        return self.character_x
    def get_y(self) :
        return self.character_y
    def get_character(self) :
        return self.character
    def move(self) :
        self.character_x += self.to_x
    def set_x(self, x) :
        self.character_x = x
    def set_y(self, y) :
        self.character_y = y
    def set_rect(self) :
        self.character_rect.left = self.character_x
        self.character_rect.top = self.character_y