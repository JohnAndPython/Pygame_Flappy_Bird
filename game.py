import pygame, random

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
        new_height = random.randint(50, 350)
        gap = random.randint(150, 170)

        self.pipe_1 = Bar("top", 1)
        self.pipe_1.rect.centerx = 500
        self.pipe_1.rect.bottom = new_height

        self.pipe_2 = Bar("bottom", 2)
        self.pipe_2.rect.centerx = 500
        self.pipe_2.rect.top = new_height + gap

        new_height = random.randint(50, 350)
        gap = random.randint(150, 170)

        self.pipe_3 = Bar("top", 3)
        self.pipe_3.rect.centerx = 780
        self.pipe_3.rect.bottom = new_height

        self.pipe_4 = Bar("bottom", 4)
        self.pipe_4.rect.centerx = 780
        self.pipe_4.rect.top = new_height + gap

        self.pipe_grp = pygame.sprite.Group()
        self.pipe_grp.add((self.pipe_1, self.pipe_2, self.pipe_3, self.pipe_4))

        # Create Player
        self.player_1 = Player(screen, height - self.ground_rect.height, 0)
        self.player_1.rect.center = (100, 250)
        self.pl_grp = pygame.sprite.GroupSingle(self.player_1)

        # Buttons
        self.resume_button = Button(screen, 25, 500, 150, 50, "Try again (Space)", 25)
        self.quit_button = Button(screen, 225, 500, 150, 50, "Quit (Q)", 30)

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
        self.game_started = False


    def play_music(self) -> None:
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    
    def _stop_music(self) -> None:
        pygame.mixer.music.stop()


    def reset(self) -> None:

        self._stop_music()

        self.pipe_grp.empty()

        # Create initial pipes
        new_height = random.randint(50, 350)
        gap = random.randint(150, 170)

        self.pipe_1.rect.centerx = 500
        self.pipe_1.rect.bottom = new_height

        self.pipe_2.rect.centerx = 500
        self.pipe_2.rect.top = new_height + gap

        new_height = random.randint(50, 350)
        gap = random.randint(150, 170)

        self.pipe_3.rect.centerx = 780
        self.pipe_3.rect.bottom = new_height

        self.pipe_4.rect.centerx = 780
        self.pipe_4.rect.top = new_height + gap

        self.pipe_grp.add((self.pipe_1, self.pipe_2, self.pipe_3, self.pipe_4))

        # Player
        self.player_1.rect.center = (100, 250)
        self.player_1.vert_speed = 0

        self.gap = 150
        self.new_height = 0

        # Score
        self.what_id = 1
        self.player_1.score = 0

        # Game state
        self.game_over = False
        self.play_sound = True
        self.game_started = False

        self.play_music()