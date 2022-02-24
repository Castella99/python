import pygame
# ---------------------------------------------------------------------

# 기본 초기화
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 540 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # screen 설정

# 화면 타이틀 설정
pygame.display.set_caption('Prototype') # 게임 이름

# FPS
clock = pygame.time.Clock()

# ---------------------------------------------------------------------

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)

# 배경 이미지 불러오기
background = pygame.image.load('/Users/hun/VScode/python/pygame_basic/20181110_180027 복사본.jpg')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('/Users/hun/VScode/python/pygame_basic/penguin.png')
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width/2 - character_width/2 # 화면 가로의 절반(중점)에 위치
character_y_pos = screen_height-character_height # 화면 세로 크기 가장 아래에 위치

# 캐릭터가 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
frame = 60
character_speed = 5 * 60 / frame

# 적 enemy 캐릭터
enemy = pygame.image.load('/Users/hun/VScode/python/pygame_basic/몽짜-cutout.png')
enemy_size = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = screen_width/2 - enemy_width/2 # 화면 가로의 절반(중점)에 위치
enemy_y_pos = screen_height/2 - enemy_height*0.75 # 화면 세로의 절반(중점)에 위치

# 폰트 정의

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    dt = clock.tick(frame) # 게임화면의 초당 프레임 수를 설정
    print('fps : '+ str(clock.get_fps()))
    # 2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT : # 캐릭터를 왼쪽
                to_x += character_speed
            elif event.key == pygame.K_UP : # 캐릭터를 왼쪽
                to_y += character_speed
            elif event.key == pygame.K_DOWN : # 캐릭터를 왼쪽
                to_y -= character_speed
        if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    # 4. 충돌 처리
    # 충돌처리를 위한 rect 정보 업데이트

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect) :
        print('충돌')
        running = False
    
    #screen.fill((255,255,255))
    screen.blit(background, (0,0)) # 배경화면을 (0,0) 위치에 삽입
    # 3. 게임 캐릭터 위치 정의
    # 5. 게임 화면에 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 생성
    character_x_pos += to_x
    character_y_pos -= to_y
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 0, 0))
    # render method parameter : 출력 정보, True, 글자 색상
    screen.blit(timer, (screen_width/2, 0))
    # 만약 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print('타임 아웃')
        running = False
    pygame.display.update() # 게임화면을 다시 그리기!

pygame.time.delay(500)
# pygame 종료
pygame.quit()