import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    deltatime = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for thing in updatable:
            thing.update(deltatime)
        
        for obj in asteroids:
            if obj.is_colliding_with(player):
                print("Game over!")
                exit()
            
            for shot in shots:
                if obj.is_colliding_with(shot):
                    obj.kill()
                    shot.kill()
                
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        
        # limit framerate to 60 FPS
        deltatime = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()