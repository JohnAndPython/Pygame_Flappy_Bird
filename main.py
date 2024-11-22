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

# Create initial pipes
pipe_1 = Bar(screen, (0,0,0), 80, 150, (450, 0))
pipe_1.rect.centerx = 500
pipe_1.rect.top = 0

pipe_2 = Bar(screen, (0,0,0), 80, 300, (450, 0))
pipe_2.rect.centerx = 500
pipe_2.rect.bottom = 600

pipe_3 = Bar(screen, (0,0,0), 80, 200, (700, 0))
pipe_3.rect.centerx = 780
pipe_3.rect.top = 0

pipe_4 = Bar(screen, (0,0,0), 80, 150, (700, 0))
pipe_4.rect.centerx = 780
pipe_4.rect.bottom = 600

pipe_grp = pygame.sprite.Group()
pipe_grp.add((pipe_1, pipe_2, pipe_3, pipe_4))

# Create Player
player_1 = Player(screen, (0,0,255), 40, 40, HEIGHT, 0)
player_1.rect.center = (100, 250)
pl_grp = pygame.sprite.GroupSingle(player_1)

dictus = dict()


while True:

    pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump()
                
    screen.fill((255,255,255))
    


    for bar in pipe_grp:
        if bar.rect.centerx <= -80:
            bar.kill()
            new_height = random.randint(50, 350)
            bar.chg_size(new_height)
            bar.rect.top = 0
            print(bar.rect.height)
            bar.rect.centerx = 440
            pipe_grp.add(bar)



    pipe_grp.update()
    pipe_grp.draw(screen)

        
    player_1.update()
    #player_1.move_down()
    player_1.draw()
    
    dictus = pygame.sprite.groupcollide(pipe_grp, pl_grp, False, False)

    pygame.display.update()
    
    clock.tick(60)