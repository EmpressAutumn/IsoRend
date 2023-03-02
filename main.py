import json
import pygame


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Tile and Grid Size
TILE_WIDTH = 64
TILE_HEIGHT = 32
GRID_WIDTH = 10
GRID_HEIGHT = 10


# Single Tile Drawing
def draw_tile(screen, x, y, color, o_x, o_y):
    # calculate the position of the top left corner of the tile
    tile_x = x * TILE_WIDTH + o_x
    tile_y = y * TILE_HEIGHT + o_y
    # calculate the position of the center of the tile
    center_x = tile_x + TILE_WIDTH / 2
    center_y = tile_y + TILE_HEIGHT / 2
    # draw the tile as a polygon
    pygame.draw.polygon(screen, color, [
        (center_x, tile_y),
        (tile_x + TILE_WIDTH, center_y),
        (center_x, tile_y + TILE_HEIGHT),
        (tile_x, center_y)
    ])


# Grid Drawing
def draw_grid(screen, o_x, o_y):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # alternate the color of the tiles
            color = WHITE if (x + y) % 2 == 0 else GREY
            draw_tile(screen, x, y, color, o_x, o_y)


def init():
    print('Initializing IsoRend...')
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("IsoRend " + json.load(open('properties.json'))['version'])

    running = True
    panning = False
    o_x, o_tx, o_y, o_ty = 0, 0, 0, 0
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

        screen.fill(BLACK)
        draw_grid(screen, o_x, o_y)
        pygame.display.update()


if __name__ == '__main__':
    version = json.load(open('properties.json'))['version']
    print(f'IsoRend Engine {version} by Atom596')
    init()
