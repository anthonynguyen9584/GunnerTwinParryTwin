import pygame,src

class Credits(src.BaseState):
    def __init__(self):
        super().__init__()
        self.reset()
        creditsFont = pygame.font.Font(self.font,25)
        self.credits = pygame.sprite.Group()
        with open('txt/Credits.txt') as f:
            lines = [line for line in f]
        for i in range(len(lines)):
            text = creditsFont.render(lines[i].translate( { ord("\n"): None } ),True,"White")
            rect = text.get_rect(center = (self.screenRect.centerx, 50 + (60*i)))
            self.credits.add(src.Text(text,rect))
        
        buttonFont = pygame.font.Font(self.font,35)
        self.ToMenu = src.Button(buttonFont,
        "Back To Menu",
        self.screenRect.centerx,
        450,
        lambda state: state.flipTo("MENU")
        )
        self.buttons = src.buttonGroup(self.ToMenu)

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
        self.credits.draw(screen)
        self.buttons.draw(screen)