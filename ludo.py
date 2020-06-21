import pygame
from pygame import MOUSEBUTTONUP, QUIT#, KEYDOWN, K_ESCAPE, 
from Player import Player
from random import randint
from time import sleep
#from collections import OrderedDict

pygame.init()

SCREEN_SIZE = 480
ICON_SIZE = SCREEN_SIZE // 15

pygame.display.set_caption("LUDO")
screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))

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

def getHomeCoin(rangu):
    for i in range(len(Players)):
        if( Players[rangu].coins[i] == Players[rangu].coins_home_pos[i] ):
            return i
    return -1          

def anyCoinOutOfHome(rangu):
    fn_CoinsOutOfHome = 0
    for i in range(len(Players)):
        print(f"Players[rangu].coins : {Players[rangu].coins}")
        if( Players[rangu].coins[i]!= Players[rangu].coins_home_pos[i] ):
            index = i
            fn_CoinsOutOfHome += 1
            print(f"index : {index}, Players[rangu].coins[index] : {Players[rangu].coins[index]}")
    if(fn_CoinsOutOfHome): # check for is not zer0
        print(f"returning index - {index}")
        return Players[rangu].coins[index]
    else:
        return (-1, -1)

def getMouseClick():
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        x,y = pygame.mouse.get_pos()
        mouse_click = (x // ICON_SIZE, y // ICON_SIZE)
        print(f"clicked on {mouse_click}")
        return mouse_click

def validateMouseClick(HomeValidation, CoinValidation, next_move, x=0, y=0):    
        if(HomeValidation and CoinValidation):
            while True:
                mouse_click = getMouseClick()
                if(((mouse_click[0] in range(y, y+6)) and (mouse_click[1] in range(x, x+6))) or mouse_click in Players[next_move].coins):
                    # return co-ordinates of the coin, if mouse click is at Home, return cordinate of available home coin
                    if((mouse_click[0] in range(y, y+6)) and (mouse_click[1] in range(x, x+6))):
                        mouse_click = Players[next_move].coins[getHomeCoin(next_move)] # getHomeCoin returns index. so, now getting position
                    return mouse_click
                else:
                    pass
                    # can play invalid click sound here
        elif(not HomeValidation and CoinValidation ):
            while True:
                mouse_click = getMouseClick()
                if(mouse_click in Players[next_move].coins):
                    return mouse_click
                else:
                    #can play invalid click sound 
                    pass

dice = [pygame.transform.scale(pygame.image.load(f"assets/dice/dice{i}.png"), (ICON_SIZE, ICON_SIZE)) for i in range(1,7)]
dice_value = 1
running = True
mouse_click = None

pygame.event.set_blocked(None)      # If None is passed - it blocks all events
pygame.event.set_allowed(pygame.MOUSEBUTTONUP) # after blocking all events, enabling required events - so that event queue doesn't track all
pygame.event.set_allowed(pygame.QUIT)

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

    # get position from coins list and update in every frame
    for color in Players:
        for x, y in Players[color].coins:
            screen.blit(Players[color].surf, (x*ICON_SIZE, y*ICON_SIZE))

    if mouse_click is None:
        p,q = Players[next_move].dice_pos
        screen.blit(dice[dice_value - 1], (p*ICON_SIZE, q*ICON_SIZE))
    else:
        x,y = Players[next_move].color_start
        if (mouse_click[0] in range(y, y+6)) and (mouse_click[1] in range(x, x+6)):   # if clicked anywhere inside color
            dice_value = randint(1,6)
            print(f"clicked on {next_move} dice, dice score-{dice_value}")
            screen.blit(dice[dice_value - 1], (p*ICON_SIZE, q*ICON_SIZE))
            pygame.display.flip()
            if(dice_value == 6):
                # 1- scenario 1 : if all 4 coins at home - move directly to start 
                print(f"Players[next_move].CoinsOutOfHome : {Players[next_move].CoinsOutOfHome}")
                if(Players[next_move].CoinsOutOfHome == 0):
                    print(f"Players[next_move].CoinsOutOfHome at start : {Players[next_move].CoinsOutOfHome}")
                    Players[next_move].coins[getHomeCoin(next_move)] = Players[next_move].start_pos
                    print(Players[next_move].coins)
                    print("moved coin to start position")
                    Players[next_move].CoinsOutOfHome += 1
                    print(f"Players[next_move].CoinsOutOfHome at end: {Players[next_move].CoinsOutOfHome}")

                # 1- scenario 2 : coins at home & outside also - based on mouse click - validate mouse click in coins list or at home, else wait for mouse click again
                elif(Players[next_move].CoinsOutOfHome and Players[next_move].CoinsOutOfHome != len(Players)):
                    print("entered scenario 2")
                    CoinToMove = validateMouseClick(HomeValidation = True, CoinValidation = True, next_move = next_move, x = x, y = y)
                    print(f" CoinToMove : {CoinToMove}")
                    if(CoinToMove in Players[next_move].coins): # move to start
                        print("entered scenario 2 - if")
                        Players[next_move].coins[getHomeCoin(next_move)] = Players[next_move].start_pos
                        print(Players[next_move].coins)
                        print("moved coin to start position")
                        Players[next_move].CoinsOutOfHome += 1
                    else:
                        print("entered scenario 2 - else")
                        Where_To = Players[next_move].move_to( CoinToMove, dice_value)
                        print(f"where to : {Where_To}")
                        Players[next_move].coins[Players[next_move].coins.index(CoinToMove)] = Where_To
                        Players[next_move].CoinsOutOfHome += 1
                        print(f" from else {Players[next_move].coins}")                        

                # 1- scenario 3 : All coins are outside - based on mouse click - validate mouse click only for in coins list?
                elif(Players[next_move].CoinsOutOfHome == len(Players)):
                    CoinToMove = validateMouseClick(HomeValidation = False, CoinValidation = True, next_move = next_move)
                    print(f" CoinToMove : {CoinToMove}")
                    Where_To = Players[next_move].move_to( CoinToMove, dice_value)
                    Players[next_move].coins[Players[next_move].coins.index(CoinToMove)] = Where_To
                    Players[next_move].CoinsOutOfHome += 1
                    print(Players[next_move].coins)                    

                # 1- scenario 4 - Another chance for rolling 6 
                mouse_click = None
                continue
            elif(Players[next_move].CoinsOutOfHome):
                CoinToMove = validateMouseClick(HomeValidation = False, CoinValidation = True, next_move = next_move)
                print(f" CoinToMove : {CoinToMove}")
                Where_To = Players[next_move].move_to( CoinToMove, dice_value)
                Players[next_move].coins[Players[next_move].coins.index(CoinToMove)] = Where_To
                Players[next_move].CoinsOutOfHome += 1
                print(Players[next_move].coins)   
                # other than 6
            print("wait for mouse click")
            pygame.event.wait()
            #logic plyer.move_to()
            next_move = get_next_move()
        mouse_click = None

    pygame.display.flip()

pygame.quit()

'''
    .
    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 7*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE + ICON_SIZE//6, 7*ICON_SIZE))

    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 8*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE, 8*ICON_SIZE))
    screen.blit(Players["red"].surf, (0*ICON_SIZE + ICON_SIZE//6, 8*ICON_SIZE))

    screen.blit(Players["green"].surf, (0*ICON_SIZE - ICON_SIZE//6, 6*ICON_SIZE))
    screen.blit(Players["blue"].surf, (0*ICON_SIZE, 6*ICON_SIZE))
    screen.blit(Players["red"].surf, (0*ICON_SIZE + ICON_SIZE//6, 6*ICON_SIZE))
    screen.blit(Players["yellow"].surf, (0*ICON_SIZE + ICON_SIZE//3, 6*ICON_SIZE))

'''