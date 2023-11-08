
import pygame

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping Man by Dylan")


player_1_x = 400
player_1_y = 650
player_1_width = 40
player_1_height = 60
player_1_vel = 8
player_1_is_jump = False
player_1_jump_count = 10

player_2_x = 200
player_2_y = 650
player_2_width = 40
player_2_height = 60
player_2_vel = 8
player_2_is_jump = False
player_2_jump_count = 10




def display_text():
    blue = (0, 0, 128)

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Use Arrow keys to move', False, blue)

    # copying the text surface object to the display surface object
    window.blit(text_surface, (250, 200))
    pygame.display.update()


startedFlag = False

run = True
while run:

    keys = pygame.key.get_pressed()
    if not (keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]) and not startedFlag:
        keys = pygame.key.get_pressed()
        display_text()
    else:
        startedFlag = True

    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Player 1
    if keys[pygame.K_LEFT] and player_1_x > player_1_vel:
        player_1_x -= player_1_vel
    if keys[pygame.K_RIGHT] and player_1_x < 800 - player_1_width - player_1_vel:
        player_1_x += player_1_vel
    if not player_1_is_jump:
        if keys[pygame.K_UP]:
            player_1_is_jump = True
    else:
        if player_1_jump_count >= -10:
            player_1_neg = 1
            if player_1_jump_count < 0:
                neg = -1
            player_1_y -= (player_1_jump_count ** 2) * 0.5 * player_1_neg
            player_1_jump_count -= 1
        else:
            player_1_is_jump = False
            player_1_jump_count = 10

    # Player 2
    if keys[pygame.K_a] and player_2_x > player_2_vel:
        player_2_x -= player_2_vel
    if keys[pygame.K_d] and player_2_x < 800 - player_2_width - player_2_vel:
        player_2_x += player_2_vel
    if not player_2_is_jump:
        if keys[pygame.K_w]:
            player_2_is_jump = True
    else:
        if player_2_jump_count >= -10:
            player_2_neg = 1
            if player_2_jump_count < 0:
                neg = -1
            player_2_y -= (player_2_jump_count ** 2) * 0.5 * player_2_neg
            player_2_jump_count -= 1
        else:
            player_2_is_jump = False
            player_2_jump_count = 10

    window.fill((255, 255, 255))
    player_1 = pygame.draw.rect(window, (0, 0, 125), (player_1_x, player_1_y, player_1_width, player_1_height))
    player_2 = pygame.draw.rect(window, (0, 0, 125), (player_2_x, player_2_y, player_2_width, player_2_height))
    floor = pygame.draw.rect(window, (0, 200, 0), [0, 700, 800, 100], 0)
    pygame.display.update()
pygame.quit()
