from Character import *
import random
import pygame

class Enemy(Character) :
    def __init__(self) :
        self.character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX1/몽짜-cutout.png')
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_speed = 20
        self.character_x = random.randint(0, 640-self.character_width)
        self.character_y = 0
        self.character_rect = self.character.get_rect()
        self.character_rect.left = self.character_x
        self.character_rect.top = self.character_y

    def down(self) :
        self.character_y += self.character_speed