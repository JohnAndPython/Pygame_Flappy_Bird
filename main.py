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
pipe_1 = Bar(screen, (200,0,0), 80, 150, (450, 0), 1, "top")
pipe_1.rect.centerx = 500
pipe_1.rect.bottom = 200

pipe_2 = Bar(screen, (50,0,0), 80, 300, (450, 0), 2, "bottom")
pipe_2.rect.centerx = 500
pipe_2.rect.top = 350

pipe_3 = Bar(screen, (0,0,200), 80, 200, (700, 0), 3, "top")
pipe_3.rect.centerx = 780
pipe_3.rect.bottom = 100

pipe_4 = Bar(screen, (0,0,50), 80, 150, (700, 0), 4, "bottom")
pipe_4.rect.centerx = 780
pipe_4.rect.top = 250

pipe_grp = pygame.sprite.Group()
pipe_grp.add((pipe_1, pipe_2, pipe_3, pipe_4))

# Create Player
player_1 = Player(screen, (0,0,255), 40, 40, HEIGHT - ground_rect.bottom, 0)
player_1.rect.center = (100, 250)
pl_grp = pygame.sprite.GroupSingle(player_1)

dictus = dict()

gap = 150
new_height = 0
a = 0

while True:

    pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump()
                
    screen.fill((50,100,200))
    

    for index, bar in enumerate(pipe_grp):
        if bar.rect.centerx <= -80:
            
            if index == 0:
                new_height = random.randint(50, 350)
                bar.rect.bottom = new_height
                gap = random.randint(120, 170)

            elif index == 1:
                bar.rect.top = new_height + gap

            bar.kill()
            bar.rect.centerx = 440
            pipe_grp.add(bar)




    pipe_grp.update()
    pipe_grp.draw(screen)

    #player_1.update()
    #player_1.draw()
    pl_grp.update()
    pl_grp.draw(screen)
    
    screen.blit(ground_surf, (0, HEIGHT - ground_rect.bottom))
    
    dictus = pygame.sprite.groupcollide(pipe_grp, pl_grp, False, False)

    print(dictus)

    pygame.display.update()
    
    clock.tick(60)