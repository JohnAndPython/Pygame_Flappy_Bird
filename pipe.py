import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surf, which) -> None:
        super().__init__()

        self.surf = surf

        if which == "top":
            self.image = pygame.image.load(r"Assets\pipe_top.png").convert_alpha()
        elif which == "bottom":
            self.image = pygame.image.load(r"Assets\pipe_bottom.png").convert_alpha()

        self.rect = self.image.get_rect()
        
        self.speed = 2

    def chg_size(self, height) -> None:
        self.rect.height = height


    def update(self) -> None:
        self.rect.centerx -= self.speed