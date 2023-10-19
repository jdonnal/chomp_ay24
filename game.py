import pygame
import sys
import random

from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen,
                 SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT,
                  SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
seagrass.set_colorkey((0, 0, 0))
sand_top.set_colorkey((0, 0, 0))

# sandy bottom
for i in range(SCREEN_WIDTH // TILE_SIZE):
    screen.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - (2 * TILE_SIZE)))
# randomly place 4 pieces of grass along the bottom of the screen
for _ in range(4):
    x = random.randint(0, SCREEN_WIDTH)
    # offset the seaweed so it looks better :)
    y = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
    screen.blit(seagrass, (x, y))
# draw the CHOMP! title
text = game_font.render("Chomp!", True, (255, 69, 0))

screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
