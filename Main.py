import pygame,src,asyncio
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Gunner Twin Perry Twin") 
# Great game

async def main():

    music = pygame.mixer.music.load("Assets/Sound/AdhesiveWombat-Night-Shade.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    states = {
        "GAMEPLAY": src.Gameplay(),
        "GAMEOVER" : src.GameOver(),
        "MENU" : src.Menu(),
        "PAUSE" : src.Pause(),
        "CREDITS" : src.Credits()
    }

    game = src.Game(screen, states, "MENU")
    await game.run()

    pygame.quit()
    exit()

asyncio.run(main())