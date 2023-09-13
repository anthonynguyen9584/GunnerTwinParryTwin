import pygame,src

class Tutorial(pygame.Surface):
    def __init__(self,w,h,font):
        super().__init__((w,h))
        self.font = font 
        self.screen = 0
        self.texts = pygame.sprite.Group()
        with open('txt/Movement.txt') as f:
            lines = [line for line in f]
        for i in range(len(lines)):
            text = self.font.render(lines[i].translate( { ord("\n"): None } ),True,"White")
            rect = text.get_rect(center = (self.get_rect().centerx, 30*i + 10))
            self.texts.add(src.Text(text,rect))

    def flip(self):
        self.texts.empty()     
        fileArgs = ['txt/Movement.txt','txt/Reflect.txt','txt/Win.txt']
        if self.screen < 2:
            self.screen += 1
        else:
            self.screen = 0
        with open(fileArgs[self.screen]) as f:
            lines = [line for line in f]
        for i in range(len(lines)):
            text = self.font.render(lines[i].translate( { ord("\n"): None } ),True,"White")
            rect = text.get_rect(center = (self.get_rect().centerx, 30*i + 10))
            self.texts.add(src.Text(text,rect))

    def draw(self,screen,x,y):
        self.fill((0,0,0))
        self.texts.draw(self)
        screen.blit(self,(x,y))