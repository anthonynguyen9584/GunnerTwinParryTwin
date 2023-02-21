import pygame,src

class GameOver(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()
        #Buttons initialization
        self.playAgain = src.Button(pygame.font.Font(None,50),
        "Play Again?",
        self.screenRect.centerx,
        self.screenRect.centery + 80,
        lambda state: state.flipTo("GAMEPLAY")
        )
        self.ToMenu = src.Button(pygame.font.Font(None,50),
        "Back To Menu",
        self.screenRect.centerx,
        self.screenRect.centery + 160,
        lambda state: state.flipTo("MENU")
        )
        self.buttons = src.buttonGroup()
        self.buttons.add(self.playAgain,self.ToMenu)
        statsFont = pygame.font.Font(None,60)
        self.stats = pygame.sprite.Group()
        for i in range(4):
            src.Stat(i,self.persist,self.screenRect.centerx,80*(i + 1),statsFont,"Purple",True).add(self.stats)

    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons.click(self)

    def update(self,dt):
        self.buttons.hover()
        self.stats.update(self.persist)

    def draw(self, screen):
        screen.fill((255,255,255))
        self.floor.draw(screen)
        self.stats.draw(screen)
        self.buttons.draw(screen)
        