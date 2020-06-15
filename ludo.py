import pygame

SIZE = 720
ICON_SIZE = 15

pygame.init()

screen = pygame.display.set_mode((SIZE, SIZE))
bg_img = pygame.transform.scale(pygame.image.load("assets/ludo_board.png"), (SIZE, SIZE))

running = True
while running:
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            running = False
    
    screen.blit(bg_img, (0 ,0))
    pygame.display.flip()

pygame.quit()