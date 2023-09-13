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

    def checkBulletCollision(self,bulletList,player,sound):
        friBulletList = [bullet for bullet in pygame.sprite.spritecollide(self, bulletList, False) if bullet.friendly]
        if len(friBulletList) != 0:
            player.kills += 1
            sound.play()
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

    def update(self,player,group,bulletList,sound):
        if self.active:
            self.move(player,group)
            self.checkBulletCollision(bulletList,player,sound)
            self.killPlayer(player)

class enemyHorde(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.spawnTime = random.randint(3 * 60,8 * 60)
        self.waveEnd = self.spawnTime + random.randint(90,2 * 60)
        self.cooldown = 60
        self.warnings = pygame.sprite.Group()
        self.warned = False

    def waveSet(self,screenW, screenH):
        for i in range((self.waveEnd - self.spawnTime) // self.cooldown):
            addedEnemy = enemy(screenW, screenH)
            self.add(addedEnemy)
            self.warnings.add(addedEnemy)
            self.warned = True
    
    def wave(self,time):
        if time < self.waveEnd and len(self.warnings.sprites()) != 0:
            self.spawnTime += self.cooldown
            actvatingEnemy = random.choice(self.warnings.sprites())
            actvatingEnemy.activate()
            pygame.sprite.Group.remove(self.warnings,actvatingEnemy)
        else:
            self.spawnTime += random.randint(5 * 60,8 * 60)
            self.waveEnd = self.spawnTime + random.randint(90,4 * 60)
            self.warned = False

    def updateGroup(self,player, bulletList,screenW, screenH,time,sound):
        if not self.warned and time > self.spawnTime - 2 * 60:
            self.waveSet(screenW, screenH)
        elif time > self.spawnTime:
            self.wave(time)
        self.update(player,self,bulletList,sound)
