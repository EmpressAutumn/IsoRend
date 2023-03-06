import pygame
from src.graphics import colors as c


class Tile:
    def __init__(self, color=None, image=None):
        self._color = color
        self._image = image

    def get_color(self):
        return self._color

    def get_image(self):
        return self._image

    def click(self):
        pass


def draw_tile(screen, pr, x, y, offset_x, offset_y, tile):  # Single Tile Drawing
    # calculate the position of the top left corner of the tile
    tile_x = (x - y) * pr.tile_dim + offset_x
    tile_y = (x + y) * pr.tile_dim / 2 + offset_y

    # calculate the position of the center of the tile
    center_x = tile_x + pr.tile_dim
    center_y = tile_y + pr.tile_dim / 2

    # alternate the color of the tiles if they don't have
    color = tile.get_color()
    if color is None:
        color = c.WHITE if (x + y) % 2 == 0 else c.GREY

    # draw the tile as a polygon
    pygame.draw.polygon(screen, color, [
        (center_x, tile_y),
        (tile_x + pr.tile_dim * 2, center_y),
        (center_x, tile_y + pr.tile_dim),
        (tile_x, center_y)
    ])


def draw_image(screen, pr, x, y, offset_x, offset_y, tile):  # Image Drawing
    tile_x = (x - y) * pr.tile_dim + offset_x
    tile_y = (x + y) * pr.tile_dim / 2 + offset_y

    try:
        img = pygame.image.load(tile.get_image()).convert()
        screen.blit(pygame.transform.scale(img, (pr.tile_dim, pr.tile_dim)), (tile_x + pr.tile_dim / 2, tile_y - pr.tile_dim / 4))
    except TypeError:
        pass


def draw_grid(screen, pr, o_x, o_y):  # Grid Drawing
    for y in range(pr.grid_height):
        for x in range(pr.grid_width):
            draw_tile(screen, pr, x, y, o_x, o_y, pr.tile_map[y][x])

    for y in range(pr.grid_height):
        for x in range(pr.grid_width):
            draw_image(screen, pr, x, y, o_x, o_y, pr.tile_map[y][x])
