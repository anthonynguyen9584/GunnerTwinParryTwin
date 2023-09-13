import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self,text,rect, rerender=False,font=None,color="White",antialais=True):
        super().__init__()
        self.image = text
        self.rect = rect

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class Stat(Text):
    def __init__(self, row,states, x,y, font, color="White", antialais=True):
        value = list(states.values())[row]
        if (row % 2 == 1):
            value = f"{value} s"
        text = font.render(f"{list(states.keys())[row]}: {value}", antialais, color)
        rect = text.get_rect(center = (x,y))
        super().__init__(text, rect)
        self.row = row
        self.color=color
        self.antialais=antialais
        self.font = font

    def update(self,states):
        self.image = self.font.render(f"{list(states.keys())[self.row]}: {list(states.values())[self.row]}",self.antialais,self.color)
