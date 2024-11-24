import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, surf, posx, posy, width, height, text_score, text_record, textsize, col=(250, 200, 0)):
        super().__init__()
        self.surf = surf
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.text_score = text_score
        self.text_record = text_record
        self.textsize = textsize
        self.col = col

        self.text_font = pygame.font.Font(None, self.textsize)
        self.text_score_surf = self.text_font.render(f"Score: {self.text_score}", False, (255, 255, 255))
        self.text_record_surf = self.text_font.render(f"Record: {self.text_record}", False, (255, 255, 255))

        self.text_score_rect = self.text_score_surf.get_rect()
        self.text_record_rect = self.text_record_surf.get_rect()

        self.button_rect = pygame.rect.Rect(self.posx, self.posy, self.width, self.height)

        self.text_score_rect.top = self.button_rect.top + 20
        self.text_score_rect.left = self.button_rect.left + 20

        self.text_record_rect.top = self.button_rect.top + 20 + textsize
        self.text_record_rect.left = self.button_rect.left + 20


    def set_score(self, score) -> None:
        self.text_score = score


    def set_record(self, record) -> None:
        self.text_record = record


    def render(self) -> None:
        self.text_score_surf = self.text_font.render(f"Score: {self.text_score}", False, (255, 255, 255))
        self.text_record_surf = self.text_font.render(f"Record: {self.text_record}", False, (255, 255, 255))


    def draw(self) -> None:
        pygame.draw.rect(self.surf, self.col, self.button_rect, border_radius=3)
        self.surf.blit(self.text_score_surf, self.text_score_rect)
        self.surf.blit(self.text_record_surf, self.text_record_rect)
