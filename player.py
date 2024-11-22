import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, lower_border, upper_border) -> None:
        super().__init__()

        self.surf = surf

        self.lower_border = lower_border
        self.upper_border = upper_border

        self.sprites = []
        self.sprites.append(pygame.image.load(r"Assets\bird_1.png").convert_alpha())
        self.sprites.append(pygame.image.load(r"Assets\bird_2.png").convert_alpha())
        self.cur_sprite = 0
        self.image = self.sprites[self.cur_sprite]
        self.rect: pygame.rect.Rect = self.image.get_rect()

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


    def animate(self) -> None:
        self.cur_sprite = round(self.cur_sprite + 0.1, 1)

        if self.cur_sprite >= len(self.sprites):
            self.cur_sprite = 0

        self.image = self.sprites[int(self.cur_sprite)]