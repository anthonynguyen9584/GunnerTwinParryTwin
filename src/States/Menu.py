import pygame,src

class Menu(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()
        titleFont = pygame.font.Font(self.font,25)
        titleText = titleFont.render("GunnerTwinParryTwin",True,"White")
        titleRect = titleText.get_rect(center = (self.screenRect.centerx, 200))
        self.title = src.Text(titleText,titleRect)
        buttonFont = pygame.font.Font(self.font,20)
        self.ToGame = src.Button(buttonFont,
        "Play",
        200,
        self.screenRect.centery,
        lambda state: state.flipTo("GAMEPLAY")
        )
        self.ToCredits = src.Button(buttonFont,
        "Credits",
        200,
        self.screenRect.centery + 80,
        lambda state: state.flipTo("CREDITS")
        )
        self.Exit = src.Button(buttonFont,
        "Close",
        200,
        self.screenRect.centery + 80*2,
        lambda state: state.exit()
        )
        self.buttons = src.buttonGroup(self.ToGame,self.ToCredits,self.Exit)
        self.tutorial = src.Tutorial(400,300,pygame.font.Font(self.font,10))
        
    def exit(self):
        self.quit = True

    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.tutorial.flip()
            self.buttons.click(self)

    def update(self,dt):
        self.buttons.hover()

    def draw(self, screen):
        screen.fill((255,255,255))
        self.floor.draw(screen)
        self.title.draw(screen)
        self.buttons.draw(screen)
        self.tutorial.draw(screen,350,250)