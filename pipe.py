import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surf, col, width, height, pos, id, which) -> None:
        super().__init__()

        self.surf = surf
        self.id = id
        self.height = height
        self.width = width
        
        if which == "top":
            self.image = pygame.image.load(r"Assets\pipe_top.png").convert_alpha()
        elif which == "bottom":
            self.image = pygame.image.load(r"Assets\pipe_bottom.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.pos = pos
        self.col = col
        
        self.speed = 2

    def chg_size(self, height) -> None:
        self.rect.height = height


    def update(self) -> None:
        self.rect.centerx -= self.speed


    # def draw(self, test) -> None:
    #     pygame.draw.rect(self.surf, self.col, self.rect)


