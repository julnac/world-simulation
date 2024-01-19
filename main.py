import pygame
import sys

from constants import *
from world import World

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH + 200, GAME_HEIGHT))
pygame.display.set_caption("World simulation")
running = True
game_state = "start_menu"


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    small_font = pygame.font.SysFont('arial', 20)
    title = font.render('World Simulation', True, (255, 255, 255))
    subtitle = small_font.render('Press ENTER to start', True, (150, 150, 150))
    screen.blit(title, ((GAME_WIDTH+200)/2 - title.get_width()/2, GAME_HEIGHT/2 - title.get_height()))
    screen.blit(subtitle, ((GAME_WIDTH+200)/2 - subtitle.get_width()/2, GAME_HEIGHT/2 + subtitle.get_height()/2 + 10 ))
    pygame.display.update()


def draw_game_over_screen(score):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    small_font = pygame.font.SysFont('arial', 20)
    title = font.render('Game Over', True, (255, 255, 255))
    score_info = small_font.render(f'Score: {score}', True, (255, 255, 255))
    restart_info = small_font.render('R - Restart', True, (150, 150, 150))
    quit_info = small_font.render('Q - Quit', True, (150, 150, 150))

    screen.blit(title, ((GAME_WIDTH+200)/2 - title.get_width()/2, GAME_HEIGHT/2 - title.get_height() - 20))
    screen.blit(score_info, ((GAME_WIDTH+200)/2 - score_info.get_width()/2, GAME_HEIGHT/2 - score_info.get_height()))
    screen.blit(restart_info, ((GAME_WIDTH+200)/2 - restart_info.get_width()/2, GAME_HEIGHT/1.9 + restart_info.get_height()))
    screen.blit(quit_info, ((GAME_WIDTH+200)/2 - quit_info.get_width()/2, GAME_HEIGHT/2 + quit_info.get_height()/2))
    pygame.display.update()


world = World()
#
# is_start_menu = True
# while is_start_menu:
#     draw_start_menu()
#     for event in pygame.event.get():
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             game_state = "game"
#             is_start_menu = False


def reset():
    global game_state, running, world
    game_state = "start_menu"
    running = True
    world = World()
    # world.round_counter = 1


while running:

    # CHECK FOR EVERY KIND OF EVENT------------
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False

        if game_state == "start_menu":
            draw_start_menu()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    game_state = "game"
                    running = True

        if game_state == "game_over":
            draw_game_over_screen(world.round_counter)
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_r]:
                    reset()

                if keys[pygame.K_q]:
                    running = False
                    pygame.quit()
                    quit()

        if game_state == "game":
            if event.type == pygame.KEYDOWN:
                screen.fill((0, 0, 0))

                if keys[pygame.K_UP]:
                    if world.human.y > 0:
                        world.human.y -= 1
                if keys[pygame.K_DOWN]:
                    if world.human.y < CELL_NUMBER - 1:
                        world.human.y += 1
                if keys[pygame.K_RIGHT]:
                    if world.human.x < CELL_NUMBER - 1:
                        world.human.x += 1
                if keys[pygame.K_LEFT]:
                    if world.human.x > 0:
                        world.human.x -= 1
                game_state = world.make_round()
                world.draw_world(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
