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

dice1 = pygame.transform.scale(pygame.image.load("assets/dice/dice1.png"), (ICON_SIZE, ICON_SIZE))
dice2 = pygame.transform.scale(pygame.image.load("assets/dice/dice2.png"), (ICON_SIZE, ICON_SIZE))
dice3 = pygame.transform.scale(pygame.image.load("assets/dice/dice3.png"), (ICON_SIZE, ICON_SIZE))
dice4 = pygame.transform.scale(pygame.image.load("assets/dice/dice4.png"), (ICON_SIZE, ICON_SIZE))
dice5 = pygame.transform.scale(pygame.image.load("assets/dice/dice5.png"), (ICON_SIZE, ICON_SIZE))
dice6 = pygame.transform.scale(pygame.image.load("assets/dice/dice6.png"), (ICON_SIZE, ICON_SIZE))

running = True
mouse_click = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.blit(bg_img, (0, 0))

    # initial Home position for each coin and dice at center
    screen.blit(green_coin, (2.5*ICON_SIZE, 1.5*ICON_SIZE))  #top  coin
    screen.blit(green_coin, (2.5*ICON_SIZE, 3.5*ICON_SIZE))  #bottom coin
    screen.blit(green_coin, (1.5*ICON_SIZE, 2.5*ICON_SIZE))  #left coin
    screen.blit(green_coin, (3.5*ICON_SIZE, 2.5*ICON_SIZE))  #right coin 

    screen.blit(yellow_coin, (2.5*ICON_SIZE, 10.5*ICON_SIZE))  #top coin
    screen.blit(yellow_coin, (2.5*ICON_SIZE, 12.5*ICON_SIZE))  #bottom coin
    screen.blit(yellow_coin, (1.5*ICON_SIZE, 11.5*ICON_SIZE))  #left coin
    screen.blit(yellow_coin, (3.5*ICON_SIZE, 11.5*ICON_SIZE))  #right coin

    screen.blit(red_coin, (10.5*ICON_SIZE, 2.5*ICON_SIZE))  #top coin
    screen.blit(red_coin, (12.5*ICON_SIZE, 2.5*ICON_SIZE))  #bottom coin
    screen.blit(red_coin, (11.5*ICON_SIZE, 1.5*ICON_SIZE))  #left coin
    screen.blit(red_coin, (11.5*ICON_SIZE, 3.5*ICON_SIZE))  #right coin

    screen.blit(blue_coin, (11.5*ICON_SIZE, 10.5*ICON_SIZE))  #top coin
    screen.blit(blue_coin, (11.5*ICON_SIZE, 12.5*ICON_SIZE))  #bottom coin
    screen.blit(blue_coin, (10.5*ICON_SIZE, 11.5*ICON_SIZE))  #left coin
    screen.blit(blue_coin, (12.5*ICON_SIZE, 11.5*ICON_SIZE))  #right coin

    screen.blit(dice1, (2.5*ICON_SIZE, 2.5*ICON_SIZE))  #dice at each Home position
    screen.blit(dice1, (2.5*ICON_SIZE, 11.5*ICON_SIZE))  #dice at each Home position
    screen.blit(dice1, (11.5*ICON_SIZE, 2.5*ICON_SIZE))  #dice at each Home position
    screen.blit(dice1, (11.5*ICON_SIZE, 11.5*ICON_SIZE))  #dice at each Home position


    pygame.display.flip()
'''
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
'''
    

pygame.quit()