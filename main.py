import json
import pygame
from tiles import red

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)


class Properties:  # Tile and Grid Size
    TILE_MAP = json.load(open("0_0.json"))
    TILE_DIM = 16
    GRID_WIDTH = len(TILE_MAP[0])
    GRID_HEIGHT = len(TILE_MAP)


class Registry:  # Dynamic Tile Registry
    def __init__(self):
        self._registrar = {}

    def register(self, key, tile):
        self._registrar.update({key: tile})

    def get_tile(self, key):
        return self._registrar[key]


TILE_REGISTRY = Registry()


def register_all():
    TILE_REGISTRY.register("0", Tile())
    TILE_REGISTRY.register("red", red.RedBlue())


class Tile:
    def __init__(self, color=None, image=None):
        self._color = color
        self._image = image

    def get_color(self):
        return self._color

    def click(self):
        pass


def draw_tile(screen, x, y, offset_x, offset_y, tile):  # Single Tile Drawing
    # calculate the position of the top left corner of the tile
    tile_x = (x - y) * Properties.TILE_DIM + offset_x
    tile_y = (x + y) * Properties.TILE_DIM / 2 + offset_y

    # calculate the position of the center of the tile
    center_x = tile_x + Properties.TILE_DIM
    center_y = tile_y + Properties.TILE_DIM / 2

    # alternate the color of the tiles if they don't have
    color = tile.get_color()
    if color is None:
        color = WHITE if (x + y) % 2 == 0 else GREY

    # draw the tile as a polygon
    pygame.draw.polygon(screen, color, [
        (center_x, tile_y),
        (tile_x + Properties.TILE_DIM * 2, center_y),
        (center_x, tile_y + Properties.TILE_DIM),
        (tile_x, center_y)
    ])


def draw_grid(screen, o_x, o_y):  # Grid Drawing
    for y in range(Properties.GRID_HEIGHT):
        for x in range(Properties.GRID_WIDTH):
            draw_tile(screen, x, y, o_x, o_y, TILE_REGISTRY.get_tile(Properties.TILE_MAP[y][x]))


def draw_gui(screen):
    pass


def init(properties):
    print('Initializing IsoRend...')
    pygame.init()
    screen = pygame.display.set_mode((properties['width'], properties["height"]), pygame.RESIZABLE)
    pygame.display.set_caption("IsoRend " + properties['version'])
    register_all()

    running = True
    panning = False
    w, h = pygame.display.get_surface().get_size()
    o_x = w / 2
    o_y = (h - Properties.TILE_DIM * Properties.GRID_WIDTH) / 2
    o_tx, o_ty = 0, 0
    tiles = []
    for y in range(Properties.GRID_HEIGHT):
        tiles.append([])
        for x in range(Properties.GRID_WIDTH):
            tiles[y].append(TILE_REGISTRY.get_tile(Properties.TILE_MAP[y][x]))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:  # Middle Click
                panning = True
                o_tx, o_ty = event.pos

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                panning = False

            elif event.type == pygame.MOUSEMOTION and panning:
                o_x += (event.pos[0] - o_tx)
                o_y += (event.pos[1] - o_ty)
                o_tx, o_ty = event.pos

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left Click
                pos_x, pos_y = pygame.mouse.get_pos()
                t_x = (pos_x - o_x) / (2 * Properties.TILE_DIM) + (pos_y - o_y) / Properties.TILE_DIM
                t_y = t_x - (pos_x - o_x) / Properties.TILE_DIM + 1
                t_x = int(t_x - 0.5)
                t_y = int(t_y - 0.5)
                if 0 <= t_x < Properties.GRID_WIDTH and 0 <= t_y < Properties.GRID_HEIGHT:
                    tiles[t_y][t_x].click()

            elif event.type == pygame.MOUSEWHEEL:
                Properties.TILE_DIM += event.y * 2
                if Properties.TILE_DIM <= 2:
                    Properties.TILE_DIM = 2

            elif event.type == pygame.WINDOWRESIZED:  # Game Window size changed
                nw, nh = pygame.display.get_surface().get_size()
                o_x *= nw / w
                o_y = (nh - Properties.TILE_DIM * Properties.GRID_WIDTH) / 2
                # o_y = nh - (o_y + TILE_DIM * GRID_WIDTH / 2) * nh / h
                w, h = nw, nh

        screen.fill(BLACK)
        draw_grid(screen, o_x, o_y)
        draw_gui(screen)
        pygame.display.update()


if __name__ == '__main__':
    prop = json.load(open('properties.json', encoding='utf-8'))
    print(f'IsoRend Engine {prop["version"]} by Atom596')
    init(prop)
