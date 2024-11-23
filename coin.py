import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()

        self.sprites = []

        for num in range(1, 9):
            self.sprites.append(pygame.image.load(fr"Assets\Coin\coin_{num}.png"))

        self.cur_sprite = 0
        self.image = self.sprites[self.cur_sprite]
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        

    def animate(self):
        self.cur_sprite += round(0.12, 2)

        if self.cur_sprite >= len(self.sprites):
            self.cur_sprite = 0

        self.image = self.sprites[int(self.cur_sprite)]