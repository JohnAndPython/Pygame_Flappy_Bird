import pygame


class Bar(pygame.sprite.Sprite):
    def __init__(self, surf, col, width, height, pos) -> None:
        super().__init__()

        self.surf = surf

        self.image = pygame.surface.Surface((width, height))
        
        self.pos = pos
        self.col = col
        self.rect = self.image.get_rect()

        self.speed = 2

    def update(self) -> None:
        self.rect.centerx -= self.speed


        

    def draw(self) -> None:
        pygame.draw.rect(self.surf, self.col, self.rect)


