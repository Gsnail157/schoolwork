from Drawable import *
import pygame
import sys
from pygame.locals import *
import random

# Color and Size Variables
SKY = (0, 255, 255)
WHITE = (255, 255, 255)
GRASS = (34, 139, 34)
LENGTH = 500
WIDTH = 600

# Initialize Pygame
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("First Game")

# Background
sky = Rectangle(0, 0, WIDTH, LENGTH * (3 / 4), SKY)
ground = Rectangle(0, LENGTH - (LENGTH * (1 / 4)), WIDTH,
                   LENGTH - (LENGTH * (3 / 4)), GRASS)


# Snowfall
snowFall = []
for i in range(500):
    snow = Snowflake(random.randrange(0, WIDTH),
                     random.randrange(-LENGTH, 0), WHITE)
    snowFall.append(snow)

NotPaused = True
while NotPaused:
    sky.draw(screen)
    ground.draw(screen)

    # Making the snow fall
    for flake in snowFall:
        flake.fall()
        flake.draw(screen)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (
            event.type == pygame.KEYDOWN and event.__dict__[
                "key"] == pygame.K_q
        ):
            pygame.quit()
            sys.exit()

        # Pausing the animation
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            if NotPaused == True:
                NotPaused = False
            else:
                NotPaused = True

    pygame.display.update()
    fpsClock.tick(30)
