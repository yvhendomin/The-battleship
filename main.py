import pygame

SIZE_FACTOR = 1
CELL = 20 * SIZE_FACTOR
WIN_SIZE_X = 683 * SIZE_FACTOR
WIN_SIZE_Y = 384 * SIZE_FACTOR
TARGET_STEP = CELL
DATA = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Field():
    """Class Field"""
    def __init__(self, player_id, x, y):
        """initializing attributes:
        player_id - whose player is field,
        start_coord - from which point it will drawn
         """
        self.player_id = player_id
        self.data = DATA
        self.length = CELL * 10
        self.x = x
        self.y = y
        self.serif = None
        self.serif2 = None
        self.pos = None
        self.pos2 = None
        self.digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

    def printf(self):
        """This method is drawing field on screen"""
        pygame.draw.rect(win, BLUE, (self.x, self.y, self.length, self.length))
        pygame.draw.rect(win, YELLOW, (self.x, self.y, TARGET_STEP, TARGET_STEP))

        for i in range(self.x, self.x + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [i, self.y], [i, self.y + self.length], 1)
        for i in range(self.y, self.y + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [self.x, i], [self.x + self.length, i], 1)


        font = pygame.font.SysFont('arial', 22 * SIZE_FACTOR, False, False)
        self.serif = font.render('A B C D F G J K L M', 1, YELLOW, BLACK)
        self.pos = self.serif.get_rect(center=(self.length // 2 + self.x, self.y - CELL // 1.5))
        win.blit(self.serif, self.pos)
        for i in range(1, 11):
            self.serif2 = font.render(self.digits[i], 1, YELLOW, BLACK)
            self.pos2 = self.serif2.get_rect(center=(self.x - CELL, self.y + (i * CELL) - CELL))
            win.blit(self.serif2, self.pos2)

pygame.init()
win = pygame.display.set_mode((WIN_SIZE_X, WIN_SIZE_Y))
pygame.display.set_caption("THE BATTLESHIP")


target_pos_x = 50
target_pos_y = 300
target_size = 40

field1 = Field(1, 50, 100)


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
