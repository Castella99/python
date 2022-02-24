from PrototypeGame import *

class dummy(PrototypeGame) : # PrototypeGame 상속
    def __init__(self) :
        # PrototypeGame 생성자 호출
        PrototypeGame.__init__(self)
        # 이벤트 루프 설정
        while self.running :
            dt = self.clock.tick(self.frame)
            print('fps : '+str(self.clock.get_fps()))
            
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False
                if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
                    if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽
                        self.character.go_right()
                    elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽
                        self.character.go_left()
                if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                        self.character.reset_to_x()
            self.screen.blit(self.character, (self.character.get_x(), self.character.get_y()))
            self.screen.blit(self.background, (0,0))
            pygame.display.update()
        pygame.time.delay(500)
        pygame.quit()

if __name__ == '__main__' :
    dummy()
        