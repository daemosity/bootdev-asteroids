import pygame

from player import Player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    deltatime = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for thing in updatable:
            thing.update(deltatime)
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        
        # limit framerate to 60 FPS
        deltatime = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()