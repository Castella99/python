import pygame
from Character import *

class PrototypeGame :
    screen_width = 640 # 스크린 가로
    screen_height = 480 # 스크린 세로
    frame = 60 # 프레임
    running = True
    # 게임 시계 설정
    clock = pygame.time.Clock()
    character_speed = 5
    character = Character(5)

    def __init__(self) :
        pygame.init() # pygame 초기화
        # 스크린 설정
        self.screen = pygame.display.set_mode((PrototypeGame.screen_width, PrototypeGame.screen_height))
        # 게임 이름 설정
        pygame.display.set_caption('PrototypeGame')
        # 백그라운드 사진 설정
        self.background = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX1/background.jpg')
        # 게임 폰트 설정
        self.game_font = pygame.font.Font(None, 40)

        # 이벤트 루프 구현 (메서드 오버라이딩)
    
   

        
        