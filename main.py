import pygame

interface_scale = 2
CELL = 20 * interface_scale
win_width = 683 * interface_scale
win_height = 384 * interface_scale
YELLOW, YELLOW_LINES, BLACK = (236, 222, 0), (255, 255, 0), (0, 0, 0)
BLUE, GREEN, RED, BROWN = (14, 20, 120), (16, 224, 13), (173, 49, 3), (76, 41, 13)


class Game(object):
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


class Player(object):
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
        self.fleet = []

        for i in range(10):
            if i == 0:
                self.ship = Ship(4, 0, 0, 0)
                self.fleet.append(self.ship)
            elif i == 1 or i == 2:
                self.ship = Ship(3, 0, 0, 0)
                self.fleet.append(self.ship)
            elif 2 < i < 6:
                self.ship = Ship(2, 0, 0, 0)
                self.fleet.append(self.ship)
            else:
                self.ship = Ship(1, 0, 0, 0)
                self.fleet.append(self.ship)


    def ships_init(self):



        def place_ships():
            pass

        def attack():
            pass

        def check_ships():
            pass

        def target():
            pass


class Enemy(Player):
    """Subclass for PC"""
    def rand_set_ships(self):
        pass

    def attack_ai(self):
        pass


class Field(object):
    """Class Field"""
    def __init__(self, player, x, y):
        """initializing attributes:
        player_id - whose player is field,
        start_coord - from which point it will drawn
         """
        self.length = CELL * 10
        self.x = x
        self.y = y
        self.tar_coord = [0, 0]
        self.player = player
        self.serif = None
        self.serif2 = None
        self.pos = None
        self.pos2 = None
        self.digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        self.x_cell = None
        self.y_cell = None
        self.color_cell = [BLUE, GREEN, RED, BROWN]

    def printf(self):
        """This method is drawing field on screen"""
        for i in range(0, 10):
            for j in range(0, 10):
                self.x_cell = self.x + j * CELL
                self.y_cell = self.y + i * CELL
                pygame.draw.rect(win, self.color_cell[self.player.data[i][j]],
                                 (self.x_cell + 1, self.y_cell + 1, CELL, CELL))

        for i in range(self.x, self.x + self.length + CELL, CELL):
            pygame.draw.line(win, YELLOW_LINES, [i, self.y], [i, self.y + self.length], 1)
        for i in range(self.y, self.y + self.length + CELL, CELL):
            pygame.draw.line(win, YELLOW_LINES, [self.x, i], [self.x + self.length, i], 1)

        font = pygame.font.SysFont('arial', 11 * interface_scale, False, False)

        self.serif = font.render('A    B    C    D    F     G    J    K    L    M', True, YELLOW, BLACK)
        self.pos = self.serif.get_rect(center=(self.length // 2 + self.x, self.y - CELL // 1.5))
        win.blit(self.serif, self.pos)
        for i in range(0, 10):
            self.serif2 = font.render(self.digits[i], True, YELLOW, BLACK)
            self.pos2 = self.serif2.get_rect(center=(self.x - CELL, self.y + CELL // 2 + i * CELL))
            win.blit(self.serif2, self.pos2)

    def target(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.tar_coord[0] > 0:
            self.tar_coord[0] -= 1
        elif keys[pygame.K_RIGHT] and self.tar_coord[0] < 9:
            self.tar_coord[0] += 1
        elif keys[pygame.K_DOWN] and self.tar_coord[1] < 9:
            self.tar_coord[1] += 1
        elif keys[pygame.K_UP] and self.tar_coord[1] > 0:
            self.tar_coord[1] -= 1

        pygame.draw.rect(win, YELLOW, (self.tar_coord[0] * CELL + self.x,
                                       self.tar_coord[1] * CELL + self.y, CELL, CELL))


class Ship(object):
    """Ship"""
    def __init__(self, count_deck, x, y, dir):
        self.count_deck = int(count_deck)
        self.dir = bool(dir)
        self.x, self.y = x, y
        self.is_it_alive = True
        self.decks_coord = [(x, y)]

    def fill_coord(self):
        """Ship creates list with coordinates of each his deck"""
        if self.dir:
            for i in range(self.count_deck):
                if i > 0:
                    self.decks_coord.append((self.x, self.y + i))
        else:
            for i in range(self.count_deck):
                if i > 0:
                    self.decks_coord.append((self.x + i, self.y))


pygame.init()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("THE BATTLESHIP")

john = Player()
pc = Enemy()
field1 = Field(john, CELL * 4, CELL * 4)
field2 = Field(pc, CELL * 20, CELL * 4)
john.ships_init()

for i in range(10):
    print(john.fleet[i].count_deck)




run = True
while run:
    pygame.time.delay(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    field1.printf()
    field2.printf()
    field2.target()
    pygame.display.update()
    win.fill((0, 0, 0))

pygame.quit()
