import pygame
import sys
from constants import *
from world import World

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("World simulation")
running = True

world = World()

while running:

    # CHECK FOR EVERY KIND OF EVENT------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            world.make_round()
            world.draw_world(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
