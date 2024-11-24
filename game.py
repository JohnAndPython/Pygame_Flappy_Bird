import pygame

from pipe import Bar
from player import Player
from coin import Coin
from button import Button

import records

class Game:
    def __init__(self, screen, height):

        # SFX
        self.crash_sfx = pygame.mixer.Sound(r"Sound\crash.wav")

        # Music
        self.music_1 = pygame.mixer.music.load(r"Music\Bittersweet Pixels.mp3")

        # Ground
        self.ground_surf = pygame.image.load(r"Assets\ground.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect()

        # Buildings
        self.buildings_surf = pygame.image.load(r"Assets\building.png").convert_alpha()
        self.buidlings_rect = self.ground_surf.get_rect()

        # Create initial pipes
        self.pipe_1 = Bar("top", 1)
        self.pipe_1.rect.centerx = 500
        self.pipe_1.rect.bottom = 200

        self.pipe_2 = Bar("bottom", 2)
        self.pipe_2.rect.centerx = 500
        self.pipe_2.rect.top = 350

        self.pipe_3 = Bar("top", 3)
        self.pipe_3.rect.centerx = 780
        self.pipe_3.rect.bottom = 100

        self.pipe_4 = Bar("bottom", 4)
        self.pipe_4.rect.centerx = 780
        self.pipe_4.rect.top = 250

        self.pipe_grp = pygame.sprite.Group()
        self.pipe_grp.add((self.pipe_1, self.pipe_2, self.pipe_3, self.pipe_4))

        # Create Player
        self.player_1 = Player(screen, height - self.ground_rect.height, 0)
        self.player_1.rect.center = (100, 250)
        self.pl_grp = pygame.sprite.GroupSingle(self.player_1)

        # Buttons
        self.resume_button = Button(screen, 25, 500, 150, 50, "Resume")
        self.quit_button = Button(screen, 225, 500, 150, 50, "Quit")

        self.gap = 150
        self.new_height = 0

        # Score
        self.best_score = records.from_file()
        self.what_id = 1
        self.score_font = pygame.font.Font(None, 35)
        self.coin_1 = Coin(10, 10)
        self.coin_grp = pygame.sprite.GroupSingle(self.coin_1)

        # Game State
        self.game_over = False
        self.play_sound = True


    def play_music(self) -> None:
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)