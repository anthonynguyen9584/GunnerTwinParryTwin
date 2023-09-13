import pygame,src

class player(pygame.sprite.Sprite):
    def __init__(self, rectPos,screenW, screenH):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Assets/playerDefault.png"), (40,40))
        self.rect = self.image.get_rect(center = rectPos)
        self.perryDefault = pygame.transform.scale(pygame.image.load("Assets/parryReady.png"), (60,60))
        self.perrySurf = self.perryDefault
        self.perryRect = self.perrySurf.get_rect(center = (self.rect.centerx,self.rect.top))
        self.perryActive = pygame.transform.scale(pygame.image.load("Assets/parryActive.png"), (60,60))
        self.perryResting = pygame.transform.scale(pygame.image.load("Assets/parryCD.png"), (60,60))
        self.clickTime = -100
        self.perry = False
        self.notResting = True
        self.borders = (screenH - 100, 50, screenW - 100)
        self.dash = 1
        self.dashintvl = 6
        self.dashTime = -10000
        self.dead = False
        self.kills = 0
    
    def draw(self,screen):
        mouseX, mouseY = pygame.mouse.get_pos()
        x, y = self.rect.x, self.rect.y
        angle = src.util.getAnglBetwObjNPoi((x,y), (mouseX,mouseY), 90)
        screen.blit(pygame.transform.rotate(self.image, angle), self.rect)
        screen.blit(pygame.transform.rotate(self.perrySurf, angle), self.perryRect)
    
    def movement(self,time):
        userInput = pygame.key.get_pressed()
        if self.dashTime > time or time < self.dashTime + self.dashintvl:
            dash = 5
            self.image = pygame.transform.scale(pygame.image.load("Assets/playerDash.png"), (40,40))
        else:
            dash = 1
            self.image = pygame.transform.scale(pygame.image.load("Assets/playerDefault.png"), (40,40))
        if userInput[pygame.K_w] and not userInput[pygame.K_s] and self.rect.y > self.borders[1]:
            self.rect.y -= 5 * dash
        if userInput[pygame.K_s] and not userInput[pygame.K_w] and self.rect.y < self.borders[0]:
            self.rect.y += 5 * dash
        if userInput[pygame.K_a] and not userInput[pygame.K_d] and self.rect.x > self.borders[1]:
            self.rect.x -= 5 * dash
        if userInput[pygame.K_d] and not userInput[pygame.K_a] and self.rect.x < self.borders[2]:
            self.rect.x += 5 * dash
    
    def perryFollow(self):
        dis = 30
        # stops perry from going to far from player
        if pygame.mouse.get_pos()[0] < 400:
            dis = -dis
        elif pygame.mouse.get_pos()[1] < 300:
            dis = -dis
        self.perryRect.center = src.util.moveToTarget(self.rect.center, 25, pygame.mouse.get_pos())
   
    def perryState(self,time):
        # 2 second of rest after activationg 
        self.notResting = time - self.clickTime > 2.5 * 60 or self.clickTime < 0
        # 1 second of activity
        if time - self.clickTime < 60:
            self.perrySurf = self.perryActive
            self.perry = True
        elif self.notResting:
            self.perrySurf = self.perryDefault
            self.perry = False
        else:
            self.perrySurf = self.perryResting
            self.perry = False
    
    def update(self,time):
        self.movement(time)
        self.perryState(time)
        self.perryFollow()
