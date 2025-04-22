import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
from shoot import *
import sys

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

    

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    asteroidfield_group = pygame.sprite.Group()
    shoot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group, asteroidfield_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (drawable_group, updatable_group, shoot_group)

    player = Player(player_x, player_y, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
    
        screen.fill("black")


        for thing in drawable_group:
            thing.draw(screen)

        for thing in updatable_group:
            thing.update(dt)
            #print(f"Number of asteroids in 'asteroids_group': {len(asteroids_group)}")
            #print(f"Number of asteroids in 'asteroidfield_group': {len(asteroidfield_group)}")


        for asteroid in asteroidfield_group:
            if player.collision(asteroid):
                print("GAME OVER")
                sys.exit()

            for bullet in shoot_group:
                if bullet.collision(asteroid):
                    asteroid.split()

        pygame.display.flip()
        
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()
