import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surf, col, width, height, pos) -> None:
        super().__init__()

        self.surf = surf

        self.height = height
        self.width = width
        self.image = pygame.surface.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.pos = pos
        self.col = col
        
        self.speed = 2

    def chg_size(self, height) -> None:
        self.rect.height = height


    def update(self) -> None:
        self.rect.centerx -= self.speed


    def draw(self) -> None:
        pygame.draw.rect(self.surf, self.col, self.rect)


