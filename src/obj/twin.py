import pygame,random,src

class twin(pygame.sprite.Sprite):
    def nextIndex(currIndex,isCounterClockwise, max):
        if isCounterClockwise:
            if currIndex == max:
                return 0
            else:
                return currIndex + 1
        else:
            if currIndex == 0:
                return 3
            else:
                return currIndex - 1

    def __init__(self, speed,timeStart):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Assets/gunner.png"), (50,50))
        self.isCounterClockwise = random.randint(0,1) == 0
        self.path = src.util.getCornerPoints((25,25),725,525)
        self.nextCorner = random.choice(self.path)
        self.prevCorner = self.path[twin.nextIndex(self.path.index(self.nextCorner), self.isCounterClockwise, 3)]
        xDis, yDis = src.util.getDisBetwPoints(self.prevCorner, self.nextCorner)
        dis = 0
        if xDis > 0:
            dis = xDis
        elif yDis > 0:
            dis = yDis
        self.rect = self.image.get_rect(center = src.util.moveToTarget(self.prevCorner, 500, self.nextCorner))
        self.speed = speed
        self.lastShot = random.randint(1000,7000) + timeStart
        self.nextShot = self.lastShot
        self.Shotintvl = random.randint(1000,4000)
        self.cooldown = 500

    def moveInPath(self):
        if self.rect.center != self.nextCorner:
            self.rect.center = src.util.moveToTarget(self.rect.center, self.speed, self.nextCorner)
        else:
            self.prevCorner = self.nextCorner
            self.nextCorner = self.path[twin.nextIndex(self.path.index(self.nextCorner), self.isCounterClockwise, 3)]
            self.isCounterClockwise = random.randint(0,1) == 0   

    def shoot(self, time, bulletGroup, obj):
        if time < self.nextShot:
            return
        angle = src.util.getAnglBetwObjNPoi((self.rect.x, self.rect.y), (obj.rect.x, obj.rect.y), 90)
        bulletGroup.add(src.bullet(self.rect.center,angle, random.randint(3,10)))
        if self.nextShot >= (self.lastShot + self.Shotintvl):
            self.nextShot += self.cooldown
        else:
            self.lastShot = self.nextShot
            self.nextShot += random.randint(2000,3000)

    def draw(self, obj,screen):
        objX, objY = obj.rect.x, obj.rect.y
        x, y = self.rect.x, self.rect.y
        angle = src.util.getAnglBetwObjNPoi((x,y), (objX,objY), 90)
        screen.blit(pygame.transform.rotate(self.image, angle), self.rect)
