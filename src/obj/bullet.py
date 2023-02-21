import pygame,math,src

class bullet(pygame.sprite.Sprite):
    def __init__(self, rectPos, angle, velocity):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Assets/bullet.png"), (30,30)), angle)
        self.rect = self.image.get_rect(center = rectPos)
        self.angle = ((angle + 90) * math.pi)/-180
        self.velocity = velocity
        self.friendly = False

# Change direction and become friendly if perried
    def checkIfPerried(self, player):
        if self.rect.colliderect(player.perryRect) and player.perry:
            mouseX, mouseY = pygame.mouse.get_pos()
            x, y = player.rect.x, player.rect.y
            self.angle = (src.util.getAnglBetwObjNPoi((x,y), (mouseX,mouseY), 0) * math.pi)/-180
            self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Assets/bulletParried.png"), (30,30)),src.util.getAnglBetwObjNPoi((x,y), (mouseX,mouseY), 90))
            self.friendly = True

    def killPlayer(self,player):
        if self.rect.colliderect(player.rect):
            player.dead = True

    def update(self,player,screenW, screenH):
        if not self.friendly:
            self.killPlayer(player)
        if self.rect.y < 0 or self.rect.y > screenH or self.rect.x < 0 or self.rect.x > screenW:
            self.kill()
        self.checkIfPerried(player)
        self.rect.y += self.velocity * math.sin(self.angle)
        self.rect.x += self.velocity * math.cos(self.angle)
