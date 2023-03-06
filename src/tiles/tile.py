from src.properties import Properties as Pr
import pygame
from src.img import colors as c


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
    tile_x = (x - y) * Pr.TILE_DIM + offset_x
    tile_y = (x + y) * Pr.TILE_DIM / 2 + offset_y

    # calculate the position of the center of the tile
    center_x = tile_x + Pr.TILE_DIM
    center_y = tile_y + Pr.TILE_DIM / 2

    # alternate the color of the tiles if they don't have
    color = tile.get_color()
    if color is None:
        color = c.WHITE if (x + y) % 2 == 0 else c.GREY

    # draw the tile as a polygon
    pygame.draw.polygon(screen, color, [
        (center_x, tile_y),
        (tile_x + Pr.TILE_DIM * 2, center_y),
        (center_x, tile_y + Pr.TILE_DIM),
        (tile_x, center_y)
    ])


def draw_grid(screen, o_x, o_y):  # Grid Drawing
    for y in range(Pr.GRID_HEIGHT):
        for x in range(Pr.GRID_WIDTH):
            draw_tile(screen, x, y, o_x, o_y, Pr.TILE_MAP[y][x])
