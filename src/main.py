import json
import pygame
from properties import Properties as Pr
from registry import registries as r
from img import colors as c
from tiles import tile


def draw_gui(screen):
    pass


def init_gameloop(properties):
    print('Initializing IsoRend...')
    pygame.init()
    screen = pygame.display.set_mode((properties['width'], properties["height"]), pygame.RESIZABLE)
    pygame.display.set_caption("IsoRend " + properties['version'])
    r.register_all()
    pr = Pr()

    panning = False
    w, h = pygame.display.get_surface().get_size()
    o_x = w / 2
    o_y = (h - pr.tile_dim * pr.grid_width) / 2
    o_tx, o_ty = 0, 0

    running = True
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
                t_x = (pos_x - o_x) / (2 * pr.tile_dim) + (pos_y - o_y) / pr.tile_dim
                t_y = t_x - (pos_x - o_x) / pr.tile_dim + 1
                t_x = int(t_x - 0.5)
                t_y = int(t_y - 0.5)
                if 0 <= t_x < pr.grid_width and 0 <= t_y < pr.grid_height:
                    pr.tile_map[t_y][t_x].click()

            elif event.type == pygame.MOUSEWHEEL:
                pr.tile_dim += event.y * 2
                if pr.tile_dim <= 2:
                    pr.tile_dim = 2

            elif event.type == pygame.WINDOWRESIZED:  # Game Window size changed
                nw, nh = pygame.display.get_surface().get_size()
                o_x *= nw / w
                o_y = (nh - pr.tile_dim * pr.grid_width) / 2
                # o_y = nh - (o_y + TILE_DIM * GRID_WIDTH / 2) * nh / h
                w, h = nw, nh
        try:
            screen.fill(c.BLACK)
            tile.draw_grid(screen, pr, o_x, o_y)
            draw_gui(screen)
            pygame.display.update()
        except pygame.error:
            break


if __name__ == '__main__':
    prop = json.load(open('properties.json', encoding='utf-8'))
    print(f'IsoRend Engine {prop["version"]} by Atom596')
    init_gameloop(prop)
