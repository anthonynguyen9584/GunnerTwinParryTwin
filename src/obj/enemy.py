import pygame,random,math,src

class enemy(pygame.sprite.Sprite):
    def __init__(self,screenW, screenH):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Assets/Warning.png"),(50,50))
        if random.randint(0,1) == 0:
            initPos = (50, random.randint(50,screenH - 100))
        else:
            initPos = (random.randint(50,screenH - 100), 50)
        self.rect = self.image.get_rect(center= initPos)
        self.active = False

    def activate(self):
        self.image = pygame.transform.scale(pygame.image.load("Assets/enemy.png"),(50,50))
        self.active = True

    def move(self,player,enemies):
        angle = (src.util.getAnglBetwObjNPoi(self.rect, player.rect, 0) * math.pi)/-180
        self.rect.x += 3 * math.cos(angle)
        self.rect.y += 3 * math.sin(angle)

    def checkBulletCollision(self,bulletList,player):
        friBulletList = [bullet for bullet in pygame.sprite.spritecollide(self, bulletList, False) if bullet.friendly]
        if len(friBulletList) != 0:
            player.kills += 1
            self.kill()

    def killPlayer(self,player):
        if self.rect.colliderect(player.rect):
            player.dead = True

    def draw(self,player,screen):
        if player.rect.x < self.rect.x:
            self.image = pygame.transform.flip(self.image,True,False)
        screen.blit(self.image, self.rect)

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self,player,group,bulletList):
        if self.active:
            self.move(player,group)
            self.checkBulletCollision(bulletList,player)
            self.killPlayer(player)

class enemyHorde(pygame.sprite.Group):
    def __init__(self,timeStart):
        super().__init__()
        self.spawnTime = random.randint(3000,8000) + timeStart
        self.waveEnd = self.spawnTime + random.randint(1500,2000)
        self.cooldown = 500
        self.warnings = pygame.sprite.Group()
        self.warned = False

    def waveSet(self,screenW, screenH):
        for i in range((self.waveEnd - self.spawnTime) // self.cooldown):
            addedEnemy = enemy(screenW, screenH)
            self.add(addedEnemy)
            self.warnings.add(addedEnemy)
            self.warned = True
    
    def wave(self):
        if pygame.time.get_ticks() < self.waveEnd and len(self.warnings.sprites()) != 0:
            self.spawnTime += self.cooldown
            actvatingEnemy = random.choice(self.warnings.sprites())
            actvatingEnemy.activate()
            pygame.sprite.Group.remove(self.warnings,actvatingEnemy)
        else:
            self.spawnTime += random.randint(5000,8000)
            self.waveEnd = self.spawnTime + random.randint(1500,4000)
            self.warned = False

    def updateGroup(self,player, bulletList,screenW, screenH):
        if not self.warned and pygame.time.get_ticks() > self.spawnTime - 2000:
            self.waveSet(screenW, screenH)
        elif pygame.time.get_ticks() > self.spawnTime:
            self.wave()
        self.update(player,self,bulletList)
