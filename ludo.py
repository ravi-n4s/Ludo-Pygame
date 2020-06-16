import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from Player import Player
from random import randint
from time import sleep
#from collections import OrderedDict

pygame.init()

SCREEN_SIZE = 720
ICON_SIZE = SCREEN_SIZE // 15

pygame.display.set_caption("LUDO")
screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load(
    "assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))

Players = {
    "green": Player("green", ICON_SIZE),
    "red": Player("red", ICON_SIZE),
    "blue": Player("blue", ICON_SIZE),
    "yellow": Player("yellow", ICON_SIZE)
}
next_move = 'green'

def get_next_move():
    colors = list(Players.keys())
    return colors[(colors.index(next_move)+1) % (len(colors))]

dice = [pygame.transform.scale(pygame.image.load(f"assets/dice/dice{i}.png"), (ICON_SIZE, ICON_SIZE)) for i in range(1,7)]
dice_value = 1
running = True
mouse_click = None

while running:
    sleep(1/2)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            mouse_click = (x // ICON_SIZE, y // ICON_SIZE)
            print(f"clicked on {mouse_click}")
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.blit(bg_img, (0, 0))
    #print("blitted bg img")
    # get position from coins list and update in every frame
    for color in Players:
        for x, y in Players[color].coins:
            #print(f"{Players[color].coins} and x, y are {x} , {y}")
            screen.blit(Players[color].surf, (x*ICON_SIZE, y*ICON_SIZE))


    if mouse_click is None:
        x, y = Players[next_move].dice_pos
        screen.blit(dice[dice_value - 1], (x*ICON_SIZE, y*ICON_SIZE))
    else:
        x,y = Players[next_move].color_start
        if (mouse_click[0] in range(y, y+6)) and (mouse_click[1] in range(x, x+6)):   # if clicked anywhere inside color
            dice_value = randint(1,6)
            print(f"clicked on {next_move} dice, dice score-{dice_value}")

            if(dice_value == 6):
                Players[next_move].coins[0] = Players[next_move].start_pos
                print(Players[color].coins)
                print("moved coin to start position")
                continue

            #logic plyer.move_to()
            
            next_move = get_next_move()
        mouse_click = None

    pygame.display.flip()

pygame.quit()