import pygame, sys, random
import records
from game import Game

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

main_game = Game(screen, HEIGHT)
main_game.play_music()

while True:

    pygame.display.set_caption(f"{clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not main_game.game_over:
                main_game.player_1.jump()

        elif event.type == pygame.MOUSEBUTTONDOWN and main_game.quit_button.collide_mouse:
            if pygame.mouse.get_pressed()[0] and main_game.game_over:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and main_game.resume_button.collide_mouse:
            if pygame.mouse.get_pressed()[0] and main_game.game_over:
                print("Hellow")
                main_game.reset()

    
    for index, bar in enumerate(main_game.pipe_grp):
        # Score logic
        if main_game.player_1.rect.left > bar.rect.right and bar.id == main_game.what_id and main_game.player_1.can_score:
            if main_game.player_1.can_score:
                main_game.player_1.can_score = False
                main_game.player_1.score += 1

                if main_game.what_id == 1:
                    main_game.what_id = 3
                    main_game.player_1.can_score = True
                elif main_game.what_id == 3:
                    main_game.what_id = 1
                    main_game.player_1.can_score = True
                
        # Remove pipe/bar from group if its centerx position if centerx <= -80 px
        # Add removed pipe at the and of the gruop with randomized height
        if bar.rect.centerx <= -80:
            if index == 0:
                new_height = random.randint(50, 350)
                bar.rect.bottom = new_height
                main_game.gap = random.randint(150, 170)
                
            elif index == 1:
                bar.rect.top = new_height + main_game.gap

            bar.kill()
            bar.rect.centerx = 440
            main_game.pipe_grp.add(bar)

    # Check for Game Over
    if (pygame.sprite.groupcollide(main_game.pipe_grp, main_game.pl_grp, False, False)) or (main_game.player_1.rect.bottom >= HEIGHT - main_game.ground_rect.height):
        main_game.game_over = True
        if main_game.play_sound:
            main_game.crash_sfx.play()
            pygame.mixer_music.fadeout(3000)

            if main_game.player_1.score > main_game.best_score:
                main_game.best_score = main_game.player_1.score
                records.write_record_tofile(main_game.best_score)

            main_game.play_sound = False
            

    screen.fill((0,200,200))

    # Update pipes and player
    main_game.pipe_grp.update(main_game.game_over)
    main_game.pl_grp.update()

    # Draw buildings, pipes, player and Coin
    screen.blit(main_game.buildings_surf, (0, 0))
    main_game.pipe_grp.draw(screen)
    main_game.pl_grp.draw(screen)
    main_game.coin_grp.draw(screen)

    if main_game.game_over:
        mouse_pos = pygame.mouse.get_pos()
        if main_game.quit_button.button_rect.collidepoint(mouse_pos):
            main_game.quit_button.set_color((200, 255, 0))
            main_game.quit_button.collide_mouse = True
        else:
            main_game.quit_button.set_color((250, 200, 0))
            main_game.quit_button.collide_mouse = False

        if main_game.resume_button.button_rect.collidepoint(mouse_pos):
            main_game.resume_button.set_color((200, 255, 0))
            main_game.resume_button.collide_mouse = True
        else:
            main_game.resume_button.set_color((250, 200, 0))
            main_game.resume_button.collide_mouse = False

        main_game.resume_button.draw()
        main_game.quit_button.draw()

    main_game.coin_1.animate()

    # Animate player
    if not main_game.game_over:
        main_game.player_1.animate()
    else:
        main_game.player_1.death_animation()
    
    # Draw ground
    screen.blit(main_game.ground_surf, (0, HEIGHT - main_game.ground_rect.bottom))

    # Draw Score
    screen.blit(main_game.score_font.render(f"{main_game.player_1.score}".zfill(4), False, (255, 255, 100)), (35, 12))

    pygame.display.update()
    
    clock.tick(60)