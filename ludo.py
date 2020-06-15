import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE

pygame.init()

SCREEN_SIZE = 720
ICON_SIZE = SCREEN_SIZE // 15

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))

green_coin = pygame.transform.scale(pygame.image.load("assets/coins/green_coin.png"), (ICON_SIZE, ICON_SIZE))
red_coin = pygame.transform.scale(pygame.image.load("assets/coins/red_coin.png"), (ICON_SIZE, ICON_SIZE))
blue_coin = pygame.transform.scale(pygame.image.load("assets/coins/blue_coin.png"), (ICON_SIZE, ICON_SIZE))
yellow_coin = pygame.transform.scale(pygame.image.load("assets/coins/yellow_coin.png"), (ICON_SIZE, ICON_SIZE))
running = True
mouse_click = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.blit(bg_img, (0, 0))
    for i in range(15):
        screen.blit(green_coin, (i*ICON_SIZE, 6*ICON_SIZE))
    for i in range(15):
        screen.blit(red_coin, (8*ICON_SIZE, i*ICON_SIZE))
    for i in range(15):
        screen.blit(blue_coin, (i*ICON_SIZE, 8*ICON_SIZE))
    for i in range(15):
        screen.blit(yellow_coin, (i*ICON_SIZE, 7*ICON_SIZE))
    for i in range(15):
        screen.blit(yellow_coin, (6*ICON_SIZE, i*ICON_SIZE))
    for i in range(15):
        screen.blit(blue_coin, (7*ICON_SIZE, i*ICON_SIZE))
    pygame.display.flip()
>>>>>>> fe0b6c97df7e0c46d574328e173ab0d4d2f8da1c
