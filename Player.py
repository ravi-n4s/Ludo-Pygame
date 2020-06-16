import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super(Player, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/coins/{self.color}_coin.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()

        self.board = [(6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6),
                      (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8),
                      (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13),
                      (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8),
                      (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1)]
        if self.color ==  "green":
            self.color_start = (0,0)
            self.start_pos = (1,6)
            self.coins = [(2.5, 1.5), (2.5, 3.5), (1.5, 2.5), (3.5, 2.5)]
            self.dice_pos = (2.5, 2.5)
            self.final_board = [(i,7) for i in range(1,7)]
        elif self.color == "red":
            self.color_start = (0,9)
            self.start_pos = (8,1)
            self.coins =[(10.5, 2.5), (12.5, 2.5), (11.5, 1.5), (11.5, 3.5)]
            self.dice_pos = (11.5, 2.5)
            self.final_board = [(7,i) for i in range(1,7)]
        elif self.color == "blue":
            self.color_start = (9,9)
            self.start_pos = (13,8)
            self.coins = [(11.5, 10.5), (11.5, 12.5), (10.5, 11.5), (12.5, 11.5)]
            self.dice_pos = (11.5, 11.5)
            self.final_board = [(i,7) for i in range(8,14)]
        else:
            self.color_start = (9,0)
            self.start_pos = (6,13)
            self.coins = [(2.5, 10.5), (2.5, 12.5), (1.5, 11.5), (3.5, 11.5)]
            self.dice_pos = (2.5, 11.5)
            self.final_board = [(7,i) for i in range(8,14)]
        

    def move_to(self, coin, move):
        #coin = self.get_pos
        index = self.board.index(coin)
        if index != -1:
            return self.board[(index + move) % 52]
        else:
            return -1