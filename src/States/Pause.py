import pygame,src

class Pause(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()
        titleFont = pygame.font.Font(self.font,25)
        titleText = titleFont.render("Pause",True,"White")
        titleRect = titleText.get_rect(center = (self.screenRect.centerx, 200))
        self.title = src.Text(titleText,titleRect)
        self.ToGame = src.Button(pygame.font.Font(self.font,20),
        "Play",
        self.screenRect.centerx,
        self.screenRect.centery,
        lambda state: state.flipTo("GAMEPLAY")
        )
        self.toMenu = src.Button(pygame.font.Font(self.font,20),
        "Back to Menu",
        self.screenRect.centerx,
        self.screenRect.centery + 80,
        lambda state: state.flipTo("MENU")
        )
        self.buttons = src.buttonGroup(self.ToGame,self.toMenu)
        self.timePauseStart = pygame.time.get_ticks()

    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.buttons.click(self)

    def update(self,dt):
        self.buttons.hover()

    def draw(self, screen):
        screen.fill((255,255,255))
        self.floor.draw(screen)
        self.title.draw(screen)
        self.buttons.draw(screen)