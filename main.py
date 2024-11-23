import pygame, sys, random, json

from pipe import Bar
from player import Player
from coin import Coin
from button import Button

import records

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# SFX
crash_sfx = pygame.mixer.Sound(r"Sound\crash.wav")

# Music
music_1 = pygame.mixer.music.load(r"Music\Bittersweet Pixels.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Ground
ground_surf = pygame.image.load(r"Assets\ground.png").convert_alpha()
ground_rect = ground_surf.get_rect()

# Buildings
buildings_surf = pygame.image.load(r"Assets\building.png").convert_alpha()
buidlings_rect = ground_surf.get_rect()

# Create initial pipes
pipe_1 = Bar("top", 1)
pipe_1.rect.centerx = 500
pipe_1.rect.bottom = 200

pipe_2 = Bar("bottom", 2)
pipe_2.rect.centerx = 500
pipe_2.rect.top = 350

pipe_3 = Bar("top", 3)
pipe_3.rect.centerx = 780
pipe_3.rect.bottom = 100

pipe_4 = Bar("bottom", 4)
pipe_4.rect.centerx = 780
pipe_4.rect.top = 250

pipe_grp = pygame.sprite.Group()
pipe_grp.add((pipe_1, pipe_2, pipe_3, pipe_4))

# Create Player
player_1 = Player(screen, HEIGHT - ground_rect.height, 0)
player_1.rect.center = (100, 250)
pl_grp = pygame.sprite.GroupSingle(player_1)

# Buttons
resume_button = Button(screen, 25, 500, 150, 50, "Resume")
quit_button = Button(screen, 225, 500, 150, 50, "Quit")


gap = 150
new_height = 0

# Score
best_score = records.from_file()
what_id = 1
score_font = pygame.font.Font(None, 35)
coin_1 = Coin(10, 10)
coin_grp = pygame.sprite.GroupSingle(coin_1)

# Game State
game_over = False
play_sound = True

while True:

    pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player_1.jump()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and game_over and quit_button.collide_mouse:
                pygame.quit()
                sys.exit()
    
    for index, bar in enumerate(pipe_grp):
        # Score logic
        if player_1.rect.left > bar.rect.right and bar.id == what_id and player_1.can_score:
            if player_1.can_score:
                player_1.can_score = False
                player_1.score += 1

                if what_id == 1:
                    what_id = 3
                    player_1.can_score = True
                elif what_id == 3:
                    what_id = 1
                    player_1.can_score = True
                
        # Remove pipe/bar from group if its centerx position if centerx <= -80 px
        # Add removed pipe at the and of the gruop with randomized height
        if bar.rect.centerx <= -80:
            if index == 0:
                new_height = random.randint(50, 350)
                bar.rect.bottom = new_height
                gap = random.randint(150, 170)
                
            elif index == 1:
                bar.rect.top = new_height + gap

            bar.kill()
            bar.rect.centerx = 440
            pipe_grp.add(bar)

   

    # Chck for Game Over
    if (pygame.sprite.groupcollide(pipe_grp, pl_grp, False, False)) or (player_1.rect.bottom >= HEIGHT - ground_rect.height):
        game_over = True
        if play_sound:
            crash_sfx.play()
            pygame.mixer_music.fadeout(3000)

            if player_1.score > best_score:
                best_score = player_1.score
                records.write_record_tofile(best_score)

            play_sound = False
            

    screen.fill((0,200,200))

    # Update pipes and player
    pipe_grp.update(game_over)
    pl_grp.update()

    # Draw pipes and player and Coin
    screen.blit(buildings_surf, (0, 0))
    pipe_grp.draw(screen)
    pl_grp.draw(screen)
    coin_grp.draw(screen)

    if game_over:
        mouse_pos = pygame.mouse.get_pos()
        if quit_button.button_rect.collidepoint(mouse_pos):
            quit_button.set_color((200, 255, 0))
            quit_button.collide_mouse = True
        else:
            quit_button.set_color((250, 200, 0))
            quit_button.collide_mouse = False

        resume_button.draw()
        quit_button.draw()

    
    coin_1.animate()

    # Animate player
    if not game_over:
        player_1.animate()
    else:
        player_1.death_animation()
    
    # Draw ground
    screen.blit(ground_surf, (0, HEIGHT - ground_rect.bottom))

    # Draw Score
    screen.blit(score_font.render(f"{player_1.score}".zfill(4), False, (255, 255, 100)), (35, 12))

    pygame.display.update()
    
    clock.tick(60)