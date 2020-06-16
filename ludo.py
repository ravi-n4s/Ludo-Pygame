import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from Player import Player
from random import randint
from time import sleep

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
    sleep(1/5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            mouse_click = (x // ICON_SIZE, y // ICON_SIZE)
            print(f"clicked on {mouse_click}")
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.blit(bg_img, (0, 0))

    for color in Players:
        for x, y in Players[color].coins:
            screen.blit(Players[color].surf, (x*ICON_SIZE, y*ICON_SIZE))

    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 7*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE + ICON_SIZE//6, 7*ICON_SIZE))

    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 8*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE, 8*ICON_SIZE))
    screen.blit(Players["red"].surf, (0*ICON_SIZE + ICON_SIZE//6, 8*ICON_SIZE))

    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 6*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE, 6*ICON_SIZE))
    screen.blit(Players["red"].surf, (0*ICON_SIZE + ICON_SIZE//6, 6*ICON_SIZE))
    screen.blit(Players["yellow"].surf, (0*ICON_SIZE + ICON_SIZE//3, 6*ICON_SIZE))

    if mouse_click is None:
        x, y = Players[next_move].get_dice()
        screen.blit(dice[dice_value - 1], (x*ICON_SIZE, y*ICON_SIZE))
    else:
        x,y = Players[next_move].get_dice()
        if (mouse_click[0]  == x+0.5 or mouse_click[0]  == x-0.5) and (mouse_click[1]  == y+0.5 or mouse_click[1]  == y-0.5):
            dice_value = randint(1,6)
            print(f"clicked on {next_move} dice, dice score-{dice_value}")
            
            #logic plyer.move_to()
            
            next_move = get_next_move()
        mouse_click = None

    pygame.display.flip()

pygame.quit()