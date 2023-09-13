import pygame,src

class GameOver(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset(isInit=True)
        titleFont = pygame.font.Font(self.font,25)
        titleText = titleFont.render("Game Over!",True,"White")
        titleRect = titleText.get_rect(center = (self.screenRect.centerx, 80))
        self.title = src.Text(titleText,titleRect)
        #Buttons initialization
        buttonFont = pygame.font.Font(self.font,20)
        self.playAgain = src.Button(buttonFont,
        "Play Again?",
        self.screenRect.centerx,
        self.screenRect.centery + 140,
        lambda state: state.flipTo("GAMEPLAY")
        )
        self.ToMenu = src.Button(buttonFont,
        "Back To Menu",
        self.screenRect.centerx,
        self.screenRect.centery + 220,
        lambda state: state.flipTo("MENU")
        )
        self.buttons = src.buttonGroup()
        self.buttons.add(self.playAgain,self.ToMenu)
        statsFont = pygame.font.Font(self.font,20)
        self.stats = pygame.sprite.Group()
        for i in range(4):
            src.Stat(i,self.persist,self.screenRect.centerx,80*(i + 1) + 60,statsFont,"Purple",True).add(self.stats)

    def reset(self, isInit = False):
        super().reset()
        if(not isInit):
            pygame.mixer.Sound("Assets/Sound/PlayerDeath.ogg").play()

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
        self.title.draw(screen)
        self.stats.draw(screen)
        self.buttons.draw(screen)
        