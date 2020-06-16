import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,color,size):
        super(Player, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size,size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/coins/{self.color}_coin.png)
        
        self.rect = self.surf.get_rect()

