import pygame,pickle,os,asyncio

class Game:
    def __init__(self, screen, states, start_state):
        self.running = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.stateName = start_state
        self.state = self.states[self.stateName]
        if os.path.getsize('txt/HighScores.txt') == 0:
            return
        with open('txt/HighScores.txt',"rb") as f:
            self.state.persist["Longest Time"],self.state.persist["Most Kills"] = pickle.load(f)

    def eventLoop(self):
        for event in pygame.event.get():
            self.state.getEvent(event)

    def flipState(self):
        self.state.done = False
        prev = self.stateName
        self.stateName = self.state.nextState
        persistent = self.state.persist
        self.state = self.states[self.stateName]
        self.state.getPersistent(persistent)
        if prev != "PAUSE" and self.stateName != "PAUSE":
            self.state.reset()

    def update(self,dt):
        if self.state.quit:
            self.running = False
        elif self.state.done:
            self.flipState()
        self.state.update(dt)
        

    def draw(self):
        self.state.draw(self.screen)

    async def run(self):
        while self.running:
            dt = self.clock.tick(self.fps)
            self.eventLoop()
            self.update(dt)
            self.draw()
            pygame.display.update()
            await asyncio.sleep(0)
        