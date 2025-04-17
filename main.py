import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_x = SCREEN_WIDTH/2
    player_y = SCREEN_HEIGHT/2

    player = Player(player_x, player_y, PLAYER_RADIUS)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
    
        screen.fill("black")

        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()
