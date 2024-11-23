import pygame

class Button:
    def __init__(self, surf, posx, posy, width, height, text, col=(250, 200, 0)):
        self.surf = surf
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.text = text
        self.col = col

        self.text_font = pygame.font.Font(None, 30)
        self.text_surf = self.text_font.render(f"{self.text}", False, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect()
        self.button_rect = pygame.rect.Rect(self.posx, self.posy, self.width, self.height)

        self.text_rect.center = self.button_rect.center

        self.collide_mouse = False

    def set_color(self, col) -> None:
        self.col = col

    def draw(self) -> None:
        pygame.draw.rect(self.surf, self.col, self.button_rect, border_radius=3)
        self.surf.blit(self.text_surf, self.text_rect)
