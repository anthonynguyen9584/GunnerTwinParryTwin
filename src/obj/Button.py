import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,font,text,x,y,command,antialias=True,colorDefault="White",colorActive="Yellow"):
        super().__init__()
        self.image = font.render(text,antialias,colorDefault)
        self.rect = self.image.get_rect(center = (x,y))
        self.colorDefault = colorDefault
        self.colorActive = colorActive
        self.font = font
        self.text = text
        self.antialias = antialias
        self.command = command

    def hover(self):
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.font.render(self.text,self.antialias,self.colorDefault)
        else:
            self.image = self.font.render(self.text,self.antialias,self.colorActive)

    def click(self,state):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.command(state)

class buttonGroup(pygame.sprite.Group):
    def hover(self):
        for button in self.sprites():
            button.hover()

    def click(self,state):
        for button in self.sprites():
            button.click(state)