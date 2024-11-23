import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, which, id) -> None:
        super().__init__()

        self.which = which
        self.id = id


        if self.which == "top":
            self.image = pygame.image.load(r"Assets\pipe_top.png").convert_alpha()
        elif self.which == "bottom":
            self.image = pygame.image.load(r"Assets\pipe_bottom.png").convert_alpha()

        self.rect = self.image.get_rect()
        
        self.speed = 2


    def update(self, game_over: bool=False) -> None:
        if not game_over:
            self.rect.centerx -= self.speed