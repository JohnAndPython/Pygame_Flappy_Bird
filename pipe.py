import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, which) -> None:
        super().__init__()

        self.which = which

        if self.which == "top":
            self.image = pygame.image.load(r"Assets\pipe_top.png").convert_alpha()
        elif self.which == "bottom":
            self.image = pygame.image.load(r"Assets\pipe_bottom.png").convert_alpha()

        self.rect = self.image.get_rect()
        
        self.speed = 2


    def update(self) -> None:
        self.rect.centerx -= self.speed