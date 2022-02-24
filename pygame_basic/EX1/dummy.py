import PrototypeGame
import random
import pygame

class dummy(PrototypeGame.Prototype) : # PrototypeGame 상속
    collide = False
    def __init__(self) :
        # PrototypeGame 생성자 호출
        PrototypeGame.Prototype.__init__(self)
        # 이벤트 루프 설정
        while self.running :
            # 시계
            dt = self.clock.tick(self.frame)
            print('fps : '+str(self.clock.get_fps()))
            # 이벤트 루프문
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

            self.pointLabel = self.game_font.render(str(self.point), True, (255,0,0))
            self.timer = self.game_font.render(str(int((pygame.time.get_ticks()-self.start_ticks)/1000)), True, (0,0,255))
            self.screen.blit(self.background, (0,0)) # 스크린 배경 설정
            self.screen.blit(self.pointLabel, (0,0))
            self.screen.blit(self.timer, (self.screen_width-30,0))
            self.screen.blit(self.character.get_character(), (self.character.get_x(), self.character.get_y())) # 캐릭터 설정
            self.character.move() # 캐릭터 이벤트 결과 적용
            if self.character.get_x() < 0 :
                self.character.set_x(0)
            elif self.character.get_x() > 640 - self.character.character_width :
                self.character.set_x(640-self.character.character_width)

            self.character.set_rect() # 캐릭터 히트박스 최신화
            self.EnemyCreate() # 똥 생성 및 움직임
            self.enemy.set_rect() # 똥 히트 박스 생성

            # 충돌 처리
            if self.character.character_rect.colliderect(self.enemy.character_rect) :
                print('충돌')
                self.running = False
                self.collide = True
            if self.collide == False and self.enemy.get_y() == 480 :
                self.enemy.set_y(0)
                self.enemy.set_x(random.randint(0, 640-self.enemy.character_width))
                pygame.time.delay(500)
                self.point+=1

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

    def EnemyCreate(self) :
        self.screen.blit(self.enemy.get_character(), (self.enemy.get_x(), self.enemy.get_y()))
        self.enemy.down()
    
    def colliderect(self, enemy) :
        if self.character.character_rect.colliderect(enemy) :
            print('충돌')
            self.running = False
            self.collide = True


if __name__ == '__main__' :
    dummy()
        