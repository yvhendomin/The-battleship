import pygame

SIZE_FACTOR = 1
CELL = 20 * SIZE_FACTOR
WIN_SIZE_X = 683 * SIZE_FACTOR
WIN_SIZE_Y = 384 * SIZE_FACTOR
TARGET_STEP = CELL

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Field():
    """Class Field"""
    def __init__(self, player_id, x, y, size, data):
        """initializing attributes:
        player_id - whose player is field,
        start_coord - from which point it will drawn
         """
        self.player_id = player_id
        self.size = size
        self.data = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
        self.length = CELL * 10
        self.x = x
        self.y = y

    def printf(self):
        """This method is drawing field on screen"""
        pygame.draw.rect(win, BLUE, (self.x, self.y, self.length, self.length))
        pygame.draw.rect(win, YELLOW, (self.x, self.y, TARGET_STEP, TARGET_STEP))

        for i in range(self.x, self.x + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [i, self.y], [i, self.y + self.length], 1)
        for i in range(self.y, self.y + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [self.x, i], [self.x + self.length, i], 1)

        """font = pygame.font.SysFont('arial', 21 * SIZE_FACTOR, False, False, )
        text1 = font.render("A B C D E F G H J K", 1, YELLOW, BLACK)
        text2 = font.render("1 2 3 4 5 6 7 8 9 10", 1, YELLOW, BLACK)
        pos = text1.get_rect(center=(248, 270))
        pos2 = text2.get_rect(center=(740, 270))"""


pygame.init()
win = pygame.display.set_mode((WIN_SIZE_X, WIN_SIZE_Y))
pygame.display.set_caption("THE BATTLESHIP")

"""font = pygame.font.SysFont('arial', 21 * SIZE_FACTOR, False, False, )
text1 = font.render("A B C D E F G H J K", 1, YELLOW, BLACK)
text2 = font.render("1 2 3 4 5 6 7 8 9 10", 1, YELLOW, BLACK)
pos = text1.get_rect(center=(248, 270))
pos2 = text2.get_rect(center=(740, 270))"""

field1_pos_x = 50
fields_pos_y = 300
field2_pos_x = 540
field_width = 400
field_height = 400
target_pos_x = 50
target_pos_y = 300
target_size = 40

field1 = Field(1, 50, 100, 1, 1)


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    """keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and target_pos_x > 50:
        target_pos_x -= TARGET_STEP
    elif keys[pygame.K_RIGHT] and target_pos_x < 410:
        target_pos_x += TARGET_STEP
    elif keys[pygame.K_DOWN] and target_pos_y < 660:
        target_pos_y += TARGET_STEP
    elif keys[pygame.K_UP] and target_pos_y > 300:
        target_pos_y -= TARGET_STEP"""
    field1.printf()
    """win.fill((0, 0, 0))"""

    """win.blit(text1, pos)"""

    pygame.display.update()

pygame.quit()
