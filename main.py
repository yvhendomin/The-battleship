import pygame

SIZE_FACTOR = 2
CELL = 20 * SIZE_FACTOR
WIN_SIZE_X = 683 * SIZE_FACTOR
WIN_SIZE_Y = 384 * SIZE_FACTOR
TARGET_STEP = CELL
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
X = CELL * 3
Y = CELL * 4
TARGET_COORD = [1, 1]


class Field():
    """Class Field"""
    def __init__(self, player, x, y):
        """initializing attributes:
        player_id - whose player is field,
        start_coord - from which point it will drawn
         """
        self.length = CELL * 10
        self.x = x
        self.y = y
        self.player = player
        self.serif = None
        self.serif2 = None
        self.pos = None
        self.pos2 = None
        self.digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        self.x_cell = None
        self.y_cell = None


    def printf(self):
        """This method is drawing field on screen"""
        for i in range(0, 10):
            for j in range(0, 10):
                if self.player.data[i][j] == 0:
                    self.x_cell = self.x + j * CELL
                    self.y_cell = self.y + i * CELL
                    pygame.draw.rect(win, BLUE, (self.x_cell, self.y_cell , CELL, CELL))

        """pygame.draw.rect(win, YELLOW, (self.x, self.y, TARGET_STEP, TARGET_STEP))"""

        for i in range(self.x, self.x + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [i, self.y], [i, self.y + self.length], 1)
        for i in range(self.y, self.y + self.length + TARGET_STEP, TARGET_STEP):
            pygame.draw.line(win, YELLOW, [self.x, i], [self.x + self.length, i], 1)

        font = pygame.font.SysFont('arial', 22 * SIZE_FACTOR, False, False)
        self.serif = font.render('A B C D F G J K L M', True, YELLOW, BLACK)
        self.pos = self.serif.get_rect(center=(self.length // 2 + self.x, self.y - CELL // 1.5))
        win.blit(self.serif, self.pos)
        for i in range(0, 10):
            self.serif2 = font.render(self.digits[i], True, YELLOW, BLACK)
            self.pos2 = self.serif2.get_rect(center=(self.x - CELL, self.y + CELL // 2 + i * CELL))
            win.blit(self.serif2, self.pos2)


class Player():
    """Class player"""
    def __init__(self):
        self.status = True
        self.deck_alive = 20
        self.data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.ships = None

        def ships_init():
            pass

        def place_ships():
            pass

        def attack():
            pass

        def check_ships():
            pass


class Enemy(Player):
    """Subclass for PC"""
    def rand_set_ships(self):
        pass

    def attack_ai(self):
        pass


class Game():
    """This class uses to manage game events"""
    def __init__(self):
        self.player = None
        self.pc = None
        self.score = None
        self.winner = None
        self.main_menu = 0
        self.active_player = None

        def is_there_winner():
            pass

        def set_winner():
            pass

        def open_field():
            pass

        def congratulations():
            pass

        def return_to_menu():
            pass

        def attack_result():
            pass

        def update_score():
            pass

        def is_ship_dead():
            pass

        def add_new_players():
            pass


class Ship():
    """Ship"""
    def __init__(self, name, count_deck, direction, x, y):
        self.name = name
        self.count_deck = int(count_deck)
        self.direction = bool(direction)
        self.x = int(x)
        self.y = int(y)
        self.status = 1





pygame.init()
win = pygame.display.set_mode((WIN_SIZE_X, WIN_SIZE_Y))
pygame.display.set_caption("THE BATTLESHIP")

john = Player()
field1 = Field(john, 100, 100)



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and TARGET_COORD[0] > 0:
        TARGET_COORD[0] -= 1
    elif keys[pygame.K_RIGHT] and TARGET_COORD[0] < 10:
        TARGET_COORD[0] += 1
    elif keys[pygame.K_DOWN] and TARGET_COORD[1] < 10:
        TARGET_COORD[1] += 1
    elif keys[pygame.K_UP] and TARGET_COORD[1] > 0:
        TARGET_COORD[1] -= 1

    field1.printf()
    """win.fill((0, 0, 0))"""

    """win.blit(text1, pos)"""

    pygame.display.update()

pygame.quit()
