import pygame
import sys
import time

from pipe import Bar
from player import Player

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bar_1 = Bar(screen, (0,0,0), 80, 100, (700, 0))
bar_1.rect.centerx = 900
bar_1.rect.top = 0


bar_2 = Bar(screen, (0,0,0), 80, 300, (700, 0))
bar_2.rect.centerx = 900
bar_2.rect.bottom = 600


bar_3 = Bar(screen, (0,0,0), 80, 200, (700, 0))
bar_3.rect.centerx = 1200
bar_3.rect.top = 0


bar_4 = Bar(screen, (0,0,0), 80, 150, (700, 0))
bar_4.rect.centerx = 1200
bar_4.rect.bottom = 600





o_group = pygame.sprite.Group()
o_group.add((bar_1, bar_2, bar_3, bar_4))


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
                player_1.vert_speed = player_1.jump_speed
                

    pygame.display.update()

    screen.fill((255,255,255))
    
    o_group.update()
    o_group.draw(screen)

    for bar in o_group:
        if bar.rect.centerx <= -80:
            bar.kill()
            bar.rect.centerx = 700
            o_group.add(bar)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     player_1.update()
        #player_1.move_up()

        
    player_1.update()
    #player_1.move_down()
    player_1.draw()
    
    dictus = pygame.sprite.groupcollide(o_group, pl_grp, False, False)

    
    
    clock.tick(60)