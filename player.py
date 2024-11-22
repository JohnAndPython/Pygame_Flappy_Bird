import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, col, width, height, lower_border, upper_border) -> None:
        super().__init__()

        self.surf = surf
        self.col = col
        self.lower_border = lower_border
        self.upper_border = upper_border

        self.image = pygame.image.load(r"Assets\bird_1.png")
        self.rect = self.image.get_rect()

        self.vert_speed = 0
        self.jump_speed = -7


    def jump(self) -> None:
        self.vert_speed = self.jump_speed


    def update(self) -> None:
        self.rect.centery += self.vert_speed
        self.vert_speed = round(self.vert_speed + 0.5, 2)

        if self.rect.bottom >= self.lower_border:
            self.rect.bottom = self.lower_border

        if self.rect.top <= self.upper_border:
            self.rect.top = self.upper_border


    # def draw(self) -> None:
    #     pygame.draw.rect(self.surf, self.col, self.rect)