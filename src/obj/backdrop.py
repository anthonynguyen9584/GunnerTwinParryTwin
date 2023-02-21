import pygame,random,src

class backDrop(pygame.sprite.Sprite):
    # Method for backdrop strites like floors, walls, and corners
    def __init__(self,imgPath, size, pos, rotation = 0):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(imgPath), size), rotation)
        self.rect = self.image.get_rect(topleft = pos)
    
    def populateFloorGroup(w,h, imgPathList, screenW, screenH):
        floorGroup = pygame.sprite.Group()
        rows, columns =  screenW // w, screenH // h
        for i in range(columns):
            for o in range(rows):
                floorGroup.add(backDrop(random.choice(imgPathList), (w,h), (w * o,h * i), 90 * random.randint(0,4)))
        return floorGroup
    
    def populateWallGroup(w,h, imgPath, screenW,screenH):
        wallGroup = pygame.sprite.Group()
        rows, columns =  screenW // w, screenH // h
        for i in range(columns):
            wallGroup.add(backDrop(imgPath, (w,h), (0,h * i),270))
        for i in range(columns):
            wallGroup.add(backDrop(imgPath, (w,h), (screenW - w,h * i), 90))
        for i in range(rows):
            wallGroup.add(backDrop(imgPath, (w,h), (w * i, 0), 180))
        for i in range(rows):
            wallGroup.add(backDrop(imgPath, (w,h), (w * i, screenH - h)))
        return wallGroup

    def populateCornerGroup(w,h, imgPath, screenW,screenH):
        screenCorners = src.util.getCornerPoints((0,0), screenW, screenH)
        cornersGroup = pygame.sprite.Group()
        cornersGroup.add(backDrop(imgPath, (w,h), screenCorners[0],180))
        cornersGroup.add(backDrop(imgPath, (w,h), (screenCorners[1][0] - w, screenCorners[1][1]), 90))
        cornersGroup.add(backDrop(imgPath, (w,h), (screenCorners[2][0] - w, screenCorners[2][1] - h)))
        cornersGroup.add(backDrop(imgPath, (w,h), (screenCorners[3][0], screenCorners[3][1] - h),270))
        return cornersGroup

    def drawGroups(floor, walls, corners, surface):
        floor.draw(surface)
        walls.draw(surface)
        corners.draw(surface)
