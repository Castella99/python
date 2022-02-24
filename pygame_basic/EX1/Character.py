import pygame
import PrototypeGame

class Character :
    character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX1/penguin.png')
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x = PrototypeGame.screen_width/2 - character_width/2
    character_y = PrototypeGame.screen_height - character_height
    character_speed = 0
    to_x = 0
    def __init__(self, speed) :
        self.character_speed = speed
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