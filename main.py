import json
import pygame


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)


class Properties:
    # Tile and Grid Size
    TILE_DIM = 16
    GRID_WIDTH = 32
    GRID_HEIGHT = 32


# Single Tile Drawing
def draw_tile(screen, x, y, color, offset_x, offset_y):
    # calculate the position of the top left corner of the tile
    tile_x = (x - y) * Properties.TILE_DIM + offset_x
    tile_y = (x + y) * Properties.TILE_DIM / 2 + offset_y
    # calculate the position of the center of the tile
    center_x = tile_x + Properties.TILE_DIM
    center_y = tile_y + Properties.TILE_DIM / 2
    # draw the tile as a polygon
    pygame.draw.polygon(screen, color, [
        (center_x, tile_y),
        (tile_x + Properties.TILE_DIM * 2, center_y),
        (center_x, tile_y + Properties.TILE_DIM),
        (tile_x, center_y)
    ])


# Grid Drawing
def draw_grid(screen, o_x, o_y):
    for y in range(Properties.GRID_HEIGHT):
        for x in range(Properties.GRID_WIDTH):
            # alternate the color of the tiles
            color = WHITE if (x + y) % 2 == 0 else GREY
            draw_tile(screen, x, y, color, o_x, o_y)


def draw_gui(screen):
    print("Not yet implemented")


def init(properties):
    print('Initializing IsoRend...')
    pygame.init()
    screen = pygame.display.set_mode((properties['width'], properties["height"]), pygame.RESIZABLE)
    pygame.display.set_caption("IsoRend " + properties['version'])

    running = True
    panning = False
    w, h = pygame.display.get_surface().get_size()
    o_x = w / 2
    o_y = (h - Properties.TILE_DIM * Properties.GRID_WIDTH) / 2
    o_tx, o_ty = 0, 0
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
        # draw_gui(screen)
        pygame.display.update()


if __name__ == '__main__':
    prop = json.load(open('properties.json', encoding='utf-8'))
    print(f'IsoRend Engine {prop["version"]} by Atom596')
    init(prop)
