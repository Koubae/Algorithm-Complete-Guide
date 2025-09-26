import pygame, sys, random
from collections import deque
from tkinter import messagebox, Tk

# ============= < GRAPH SIZE > ============= #
size = (width, height) = 1_280, 960
cols, rows = 64, 48  # 64, 48
w = width // cols # 10
h = height // rows # 10

# ============= < PYGAME INITIALIZATION > ============= #
pygame.init()
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption("Dijktdtra's Path Finder")

# ============= < ALGORITHM SETTINGS > ============= #
GRID = []
neighbour, visited = deque(), []
SHORTEST_PATH = []
START = None
TARGET = None
TOTAL_NODES = cols * rows   # FAQ: 3,072 Nodes if normal size or 12288 if doubled it

# ====== < SPEED CONSTANTS > ====== #
FLASH = TOTAL_NODES  # 3,072
SUPER_FAST = TOTAL_NODES // 24  # 128
FAST = SUPER_FAST // 4 # 32
MEDIUM = FAST // 4 # 8
SLOW = MEDIUM // 4  # 2

# ============= < COLOR PALETTE > ============= #
COLOR_SET = {
    'grid': (44, 62, 80),
    'start': (255, 255, 0),
    'target': (252, 36, 3),
    'wall': (0, 0, 0),
    'visited': (3, 123, 252),
    'current': [(173, 255, 47), (255, 165, 0)],  # QST: Index 0 = Background | Index 1 = Circle on top
    'shortest_path': (32, 252, 3)
}


class Node:
    def __init__(self, y, x):
        self.y, self.x = y, x
        self.neighbors = []
        self.prev = None
        self._wall = False
        self.visited = False
        self.start = False
        self.target = False

    @property
    def wall(self):
        return self._wall

    @wall.setter
    def wall(self, bool_):
        if not self.start and not self.target:
            if bool_ == 'toggle':
                if self._wall:
                    self._wall = False
                else:
                    self._wall = True
            elif bool_ == 'mouse_motion':
                self._wall = True

    def show(self, SCREEN, col, shape=1):
        if self._wall:
            col = COLOR_SET['wall']
        if shape == 1:
            pygame.draw.rect(SCREEN, col, (self.y * w, self.x * h, w - 1, h - 1))
        else:
            pygame.draw.circle(SCREEN, col, (self.y * w + w // 2, self.x * h + h // 2), w // 3)

    def add_neighbors(self):
        if self.y < cols - 1:
            self.neighbors.append(GRID[self.y + 1][self.x])
        if self.y > 0:
            self.neighbors.append(GRID[self.y - 1][self.x])
        if self.x < rows - 1:
            self.neighbors.append(GRID[self.y][self.x + 1])
        if self.x > 0:
            self.neighbors.append(GRID[self.y][self.x - 1])


def make_double():
    global cols
    global rows
    global w
    global h
    cols, rows = cols * 2, rows * 2
    w = width // cols  # 10
    h = height // rows  # 10


def make_grid(double_nodes=False):
    if double_nodes:
        make_double()
    for y in range(cols):
        row = [Node(y, x) for x in range(rows)]
        GRID.append(row)
    for y in range(cols):
        for x in range(rows):
            GRID[y][x].add_neighbors()


def random_cols():
    return random.randint(0, 63)


def random_rows():
    return random.randint(0, 47)


def initialize():
    global START
    global TARGET
    START = GRID[random_cols()][random_rows()]
    START.wall, START.start = False, True
    neighbour.append(START)
    START.visited = True

    TARGET = GRID[random_cols()][random_rows()]
    TARGET.wall, TARGET.target = False, True


def reset():
    GRID[:] = []
    visited[:] = []
    SHORTEST_PATH[:] = []

    make_grid()
    initialize()


def main(speed=MEDIUM):
    TARGET_FOUND = False
    noflag = True
    find_path = False
    new_game = False

    def clickWall(pos, mouse_motion=None):
        y = pos[0] // w
        x = pos[1] // h
        if not mouse_motion:
            GRID[y][x].wall = 'toggle'
        else:
            GRID[y][x].wall = 'mouse_motion'

    while True:

        if new_game:
            TARGET_FOUND = False
            noflag = True
            find_path = False
            new_game = False
            reset()

        # FAQ:================================ < Event Handler > =========================================== #
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            event_ = event.type
            if event_ == pygame.QUIT:  # FAQ: Quit Game
                pygame.quit()
                print('==='*15 + ' < ' + 'GAME OVER' + ' > ' + '==='*15)
                sys.exit()

            if not find_path:  # FAQ: Run only if Algorithm is not running

                if event_ == pygame.KEYDOWN:  # FAQ: Start Game
                    if event.key == pygame.K_RETURN:
                        find_path = True

                elif event_ == pygame.MOUSEMOTION or event_ == pygame.MOUSEBUTTONUP:  # FAQ: Add walls
                    mouse_event = pygame.mouse.get_pressed(3)
                    if mouse_event[0]:
                        clickWall(mouse_pos, 'mouse_motion')
                    elif not event_ == pygame.MOUSEMOTION:
                        clickWall(mouse_pos)

            elif TARGET_FOUND or not noflag:  # FAQ: Start a new Game
                if event_ == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        new_game = True
            else:
                pass

        # FAQ:============================ < Djikstra Algorithm > ================================== #
        for _ in range(speed):
            if find_path:
                if len(neighbour) > 0:
                    current = neighbour.popleft()

                    if current == TARGET:  # QST: Target Node found
                        temp = current
                        while temp.prev:
                            SHORTEST_PATH.append(temp.prev)
                            temp = temp.prev
                        if not TARGET_FOUND:
                            TARGET_FOUND = True
                            print('==='*15 + ' < ' + 'Shortest Path found!' + ' > ' + '==='*15)

                    if not TARGET_FOUND:   # FAQ: If Target is not found, keep looking for target
                        for i in current.neighbors:
                            if not i.visited and not i.wall:
                                i.visited = True
                                i.prev = current
                                neighbour.append(i)
                else:
                    if noflag and not TARGET_FOUND:  # FAQ: Game OVer
                        Tk().wm_withdraw()
                        messagebox.showinfo("Game Over", "Target node was not found!")
                        noflag = False

        # FAQ:============================ < Screen Framce Update > ================================== #
        for y in range(cols):
            for x in range(rows):
                node = GRID[y][x]
                if node in neighbour:  # FAQ: Current Node
                    node.show(SCREEN, COLOR_SET['current'][0])  # Background
                    node.show(SCREEN, COLOR_SET['current'][1], 0)  # Circle on Top
                elif node == START:
                    node.show(SCREEN, COLOR_SET['start'])
                elif node == TARGET:
                    node.show(SCREEN, COLOR_SET['target'])
                elif node.visited:
                    node.show(SCREEN, COLOR_SET['visited'])  # FAQ: Visited
                else:
                    node.show(SCREEN, COLOR_SET['grid'])  # FAQ: Whole Grid Color

                if node in SHORTEST_PATH:
                    node.show(SCREEN, COLOR_SET['shortest_path'])  # FAQ: The Shortest-Path Tree

        pygame.display.flip()


if __name__ == '__main__':
    make_grid(double_nodes=False)
    initialize()
    main(FAST)

# NOTE: Use make_grid(double_nodes=True) to double the Total Nodes in the Graph, from 3,072 to 12288 | Default 3,072
# NOTE pass SLOW | MEDIUM | FAST | SUPER_FAST | FLASH in main() func as argument to change the speed, Default is medium