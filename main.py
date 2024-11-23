import pygame
import sys
import time
import random

from pipe import Bar
from player import Player

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ground_surf = pygame.image.load(r"Assets\ground.png").convert_alpha()
ground_rect = ground_surf.get_rect()

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

gap = 150
new_height = 0

game_over = False
what_id = 1

# Score
score_font = pygame.font.Font(None, 35)

while True:

    pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player_1.jump()
                
    screen.fill((50,100,200))
    

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

    # Draw pipes and player

    pipe_grp.update(game_over)
    pl_grp.update()

    pipe_grp.draw(screen)
    pl_grp.draw(screen)

    # Anminate player
    if not game_over:
        player_1.animate()
    else:
        player_1.death_animation()
    
    # Draw ground
    screen.blit(ground_surf, (0, HEIGHT - ground_rect.bottom))
    screen.blit(score_font.render(f"{player_1.score}".zfill(4), False, (255, 255, 100)), (10, 10))

    
    
    pygame.display.update()
    
    clock.tick(60)