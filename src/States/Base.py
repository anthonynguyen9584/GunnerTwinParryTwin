import pygame,src

class BaseState():
    def __init__(self):
        self.done = False
        self.quit = False
        self.nextState = None
        self.screenRect = pygame.display.get_surface().get_rect()
        self.persist = {
            "Kills" : 0,
            "Time" : 0,
            "Most Kills" : 0,
            "Longest Time" : 0,
            "TIMESTART" : 0
        }
        self.font = "public-pixel-font/PublicPixel-z84yD.ttf"

    def getPersistent(self, persistent):
        self.persist = persistent

    def reset(self):
        self.floor = src.backDrop.populateFloorGroup(100, 100, [f"Assets/bg{x}.png" for x in range(1,4)], self.screenRect.width,self.screenRect.height)

    def getEvent(self, event):
        pass
# dt = delta time
    def update(self):
        pass

    def draw(self, screen):
        pass

    def flipTo(self,next):
        if next == "GAMEPLAY":
            self.persist["TIMESTART"] = pygame.time.get_ticks()
        self.nextState = next
        self.done = True

