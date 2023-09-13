import pygame,src,pickle

class Gameplay(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()
        self.shootSound = pygame.mixer.Sound("Assets/Sound/shoot.ogg")
        self.parrySound = pygame.mixer.Sound("Assets/Sound/Parry.ogg")
        self.dashSound = pygame.mixer.Sound("Assets/Sound/dash.ogg")
        self.deathSound = pygame.mixer.Sound("Assets/Sound/EnemyDeath.ogg")


    def reset(self):
        self.perryTwin = src.player((400, 300),self.screenRect.width,self.screenRect.height)
        self.gunnerTwin = src.twin(5)
        self.floor = src.backDrop.populateFloorGroup(100, 100, [f"Assets/bg{x}.png" for x in range(1,4)], self.screenRect.width,self.screenRect.height)
        self.walls = src.backDrop.populateWallGroup(50, 50, "Assets/wall.png", self.screenRect.width,self.screenRect.height)
        self.corners = src.backDrop.populateCornerGroup(50, 50, "Assets/wallCorner.png", self.screenRect.width,self.screenRect.height)
        self.bullets = pygame.sprite.Group()
        self.enemies = src.enemyHorde()
        self.persist["TIMESTART"] = pygame.time.get_ticks()
        self.time  = 0


    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.perryTwin.notResting:
                self.perryTwin.clickTime = self.time
                self.parrySound.play()
            if event.button == 3:
                self.perryTwin.dashTime = self.time
                self.dashSound.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.nextState = "PAUSE"
                self.done = True
# dt = delta time
    def update(self,dt):
        if self.perryTwin.dead:
            self.updateScores()
        self.perryTwin.update(self.time)
        self.gunnerTwin.update(self.bullets, self.perryTwin,self.time,self.shootSound)
        self.bullets.update(self.perryTwin,self.screenRect.width,self.screenRect.height,self.shootSound)
        self.enemies.updateGroup(self.perryTwin,self.bullets,self.screenRect.width,self.screenRect.height,self.time,self.deathSound)
        self.time += 1
        
    def updateScores(self):
        self.nextState = "GAMEOVER"
        self.persist["Kills"] = self.perryTwin.kills
        time = (pygame.time.get_ticks() - self.persist["TIMESTART"])//1000
        self.persist["Time"] = time
        self.done = True
        if (self.persist["Longest Time"] < time):
            self.persist["Longest Time"] = time
        if (self.persist["Most Kills"] < self.perryTwin.kills):
            self.persist["Most Kills"] = self.perryTwin.kills
       
        with open('txt/HighScores.txt', 'wb') as f:
            pickle.dump([self.persist["Longest Time"],self.persist["Most Kills"]], f)

    def draw(self,screen):
        screen.fill((255,255,255))
        src.backDrop.drawGroups(self.floor, self.walls, self.corners, screen)
        self.gunnerTwin.draw(self.perryTwin,screen)
        self.bullets.draw(screen)
        self.enemies.draw(screen)
        self.perryTwin.draw(screen)