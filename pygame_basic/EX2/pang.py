from PrototypeGame import *

class Pang(Prototype) :
    timeTemp = None
    spear = weapon()
    spearOn = False

    def __init__(self):
        # Prototype 상속
        super().__init__(30)
        # 게임 이름 명명
        pygame.display.set_caption('Pang')
        # 백그라운드 변수 선언
        self.background = pygame.image.load('/Users/hun/VScode/python/pygame_basic/EX2/mount__fuji-wallpaper-640x480.jpg')

        # 이벤트 루프
        while self.running :
            # 프레임 설정
            dt = self.clock.tick(self.frame)
            self.timeTemp = pygame.time.get_ticks()
            if int((self.timeTemp - self.start_ticks) % 10) == 0 :
                print('fps : '+str(self.clock.get_fps()))
            # 점수 설정
            self.pointLabel = self.game_font.render(str(self.point), True, (255,0,0))
            # 타이머 설정
            self.timer = self.game_font.render(str(int((pygame.time.get_ticks()-self.start_ticks)/1000)), True, (0,0,255))

            # 방향키 이벤트 처리
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False
                if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
                    if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽
                        self.character.go_left()
                    elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽
                        self.character.go_right()
            
                if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                        self.character.reset_to_x()
                    elif event.key == pygame.K_UP :
                        if self.spearOn == False :
                            self.spear.setXY(self.character.get_x(), self.character.get_y()-self.spear.character_height/10)
                            self.spearOn = True

            self.screen.blit(self.background, (0,0)) # 스크린 배경 설정
            self.screen.blit(self.pointLabel, (0,0)) # 점수표 표시
            self.screen.blit(self.timer, (self.screen_width-30,0)) # 타이머 표시
            self.screen.blit(self.character.get_character(), (self.character.get_x(), self.character.get_y())) # 캐릭터 설정
            self.screen.blit(self.enemy.get_character(), (self.enemy.get_x(), self.enemy.get_y())) # 풍선 설정
            self.character.move() # 캐릭터 이벤트 결과 적용

            
            # 캐릭터 범위 제한
            if self.character.get_x() < 0 :
                self.character.set_x(0)
            elif self.character.get_x() > 640 - self.character.character_width :
                self.character.set_x(640-self.character.character_width)
            
            # 키 이벤트를 통해 창을 구현
            if self.spearOn :
                self.Spear()
                if self.spear.character_y <= 0 :
                    self.spearOn = False
            
            self.character.set_rect() # 캐릭터 히트박스 최신화
            self.enemy.set_rect() # 풍선 히트 박스 생성
            
            if self.enemy.character_rect.colliderect(self.spear.character_rect) :
                print('풍선 충돌')
            
            # 충돌 처리
            if self.character.character_rect.colliderect(self.enemy.character_rect) :
                print('충돌')
                self.running = False

            

            # 풍선 생성 후 움직이는 함수
            self.Enemymove()




            pygame.display.update()
        
        self.game_font_R = pygame.font.Font(None, 100)
        self.result = self.game_font_R.render(str(self.point)+'Point', True, (0, 0, 0))
        self.result_size = self.result.get_rect().size
        self.result_width = self.result_size[0]
        self.result_height = self.result_size[1]
        self.screen.blit(self.result, (self.screen_width/2 - self.result_width/2, self.screen_height/2-self.result_height/2))
        pygame.display.update()
        pygame.time.delay(3000)
        print('점수 : %s' %self.point)
        pygame.quit() 
    
    def Enemymove(self) :
        self.screen.blit(self.enemy.get_character(), (self.enemy.get_x(), self.enemy.get_y()))

        if self.enemy.get_x() <= 0 :
            self.enemy.set_x(0)
            self.enemy.wall()
        elif self.enemy.get_x() >= 640 - self.enemy.character_width :
            self.enemy.set_x(640-self.enemy.character_width)
            self.enemy.wall()
    
        if self.enemy.get_y() >= 480 - self.enemy.character_height :
            self.enemy.set_y(480 - self.enemy.character_height)
            print('y축 방향 풍선 속도 : ', self.enemy.character_ySpeed)
            self.enemy.setYspeed(26)
            self.enemy.Updown()
        
        self.enemy.GravityAccel()
        self.enemy.move()

    def Spear(self) :
        self.screen.blit(self.spear.get_character(), (self.spear.get_x(), self.spear.get_y()))
        self.spear.move()
        self.spear.set_rect()
        print(self.spear.character_rect.left, self.spear.character_rect.top)



if __name__ == '__main__' :
    Pang()