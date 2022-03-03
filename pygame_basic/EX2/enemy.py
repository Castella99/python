from Character import *
import random
import pygame

class Enemy(Character) :
    yaccel = 0
    character_xSpeed = 0
    character_ySpeed = 0

    def __init__(self) :
        self.character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX2/balloon.png')
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_xSpeed = random.randint(-10, 10)
        self.yaccel = 1
        self.character_x = random.randint(1, 640-self.character_width)
        self.character_y = 0
        self.character_rect = self.character.get_rect()
        self.character_rect.left = self.character_x
        self.character_rect.top = self.character_y

    def move(self) :
        self.character_y += self.character_ySpeed
        self.character_x += self.character_xSpeed

    def Updown(self) :
        temp = self.character_ySpeed
        self.character_ySpeed = -temp
        
    def wall(self) :
        temp = self.character_xSpeed
        self.character_xSpeed = -temp

    def GravityAccel(self) :
        self.character_ySpeed += self.yaccel
    
    def setYspeed(self, y) :
        self.character_ySpeed = y
