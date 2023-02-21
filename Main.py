import pygame,src
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Gunner Twin Perry Twin") 

states = {
    "GAMEPLAY": src.Gameplay(),
    "GAMEOVER" : src.GameOver(),
    "MENU" : src.Menu(),
    "PAUSE" : src.Pause()
}

game = src.Game(screen, states, "MENU")
game.run()

pygame.quit()
exit()