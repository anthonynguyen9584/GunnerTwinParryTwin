import pygame,src

class Gameplay(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.perryTwin = src.player((400, 300),self.screenRect.width,self.screenRect.height)
        self.gunnerTwin = src.twin(5,self.persist["TIMESTART"])
        self.floor = src.backDrop.populateFloorGroup(100, 100, [f"Assets/bg{x}.png" for x in range(1,4)], self.screenRect.width,self.screenRect.height)
        self.walls = src.backDrop.populateWallGroup(50, 50, "Assets/wall.png", self.screenRect.width,self.screenRect.height)
        self.corners = src.backDrop.populateCornerGroup(50, 50, "Assets/wallCorner.png", self.screenRect.width,self.screenRect.height)
        self.bullets = pygame.sprite.Group()
        self.enemies = src.enemyHorde(self.persist["TIMESTART"])
        self.gameTimer = 0

    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.perryTwin.notResting:
                self.perryTwin.clickTime = pygame.time.get_ticks()
            if event.button == 3:
                self.perryTwin.dashTime = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.nextState = "PAUSE"
                self.done = True
# dt = delta time
    def update(self,dt):
        if self.perryTwin.dead:
            self.nextState = "GAMEOVER"
            self.persist["KILLS"] = self.perryTwin.kills
            time = (pygame.time.get_ticks() - self.persist["TIMESTART"])//1000
            self.persist["TIME"] = f"{time} S"
            self.done = True
        gameTimer = pygame.time.get_ticks()
        self.perryTwin.update(gameTimer)
        self.gunnerTwin.moveInPath()
        self.bullets.update(self.perryTwin,self.screenRect.width,self.screenRect.height)
        self.enemies.updateGroup(self.perryTwin,self.bullets,self.screenRect.width,self.screenRect.height)
        self.gunnerTwin.shoot(gameTimer, self.bullets, self.perryTwin)
        

    def draw(self,screen):
        screen.fill((255,255,255))
        src.backDrop.drawGroups(self.floor, self.walls, self.corners, screen)
        self.gunnerTwin.draw(self.perryTwin,screen)
        self.bullets.draw(screen)
        self.enemies.draw(screen)
        self.perryTwin.draw(screen)