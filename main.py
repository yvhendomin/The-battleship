import pygame

pygame.init()
win = pygame.display.set_mode((1366, 768))

pygame.display.set_caption("THE BATTLESHIP")


field1_pos_x = 50
fields_pos_y = 300
field2_pos_x = 540
field_width = 400
field_height = 400
target_pos_x = 50
target_pos_y = 300
target_size = 40
speed = 40

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and target_pos_x > 50:
        target_pos_x -= speed
    elif keys[pygame.K_RIGHT] and target_pos_x < 410:
        target_pos_x += speed
    elif keys[pygame.K_DOWN] and target_pos_y < 660:
        target_pos_y += speed
    elif keys[pygame.K_UP] and target_pos_y > 300:
        target_pos_y -= speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (field1_pos_x, fields_pos_y, field_width, field_height))
    pygame.draw.rect(win, (0, 0, 255), (field2_pos_x, fields_pos_y, field_width, field_height))
    pygame.draw.rect(win, (255, 255, 0), (target_pos_x, target_pos_y, target_size, target_size))

    for i in range(field1_pos_x, 490, 40):
        pygame.draw.line(win, (255, 255, 0), [i, 300], [i, 700], 1)
    for i in range(fields_pos_y, fields_pos_y + 440, 40):
        pygame.draw.line(win, (255, 255, 0), [50, i], [450, i], 1)

    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont('arial', 42, False, False,)
    text1 = font.render("A B C D E F G H J K", 1, YELLOW, BLACK)
    text2 = font.render("1 2 3 4 5 6 7 8 9 10", 1, YELLOW, BLACK)
    pos = text1.get_rect(center=(248, 270))
    pos2 = text2.get_rect(center=(740, 270))

    win.blit(text1, pos)

    pygame.display.update()

pygame.quit()
