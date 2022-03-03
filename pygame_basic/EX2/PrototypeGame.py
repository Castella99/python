import pygame
from Character import *
from enemy import *
from weapon import *

class Prototype :
    screen_width = 640 # 스크린 가로
    screen_height = 480 # 스크린 세로
    frame = 0 # 프레임
    running = True
    # 게임 시계 설정
    clock = pygame.time.Clock()
    character = None
    enemy = Enemy()
    point = 0
    game_font = None
    start_ticks = 0 # 시작 tick을 받아옴
    background = None

    def __init__(self, f) :
        self.frame = f
        self.character = Character(5*60/self.frame)
        pygame.init() # pygame 초기화
        self.game_font = pygame.font.Font(None, 40)
        # 스크린 설정
        self.screen = pygame.display.set_mode((Prototype.screen_width, Prototype.screen_height))
        # 게임 이름 설정
        # 게임 폰트 설정
        self.game_font = pygame.font.Font(None, 40)
        
        self.start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴
        # 이벤트 루프 구현 (메서드 오버라이딩)
    
   

        
        