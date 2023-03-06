import json
import copy
from registry import registries


class Properties:  # Tile and Grid Size

    def __init__(self):
        self.tile_map = []
        for y in range(len(json.load(open("maps/0_0.json")))):
            self.tile_map.append([])
            for x in range(len(json.load(open("maps/0_0.json"))[0])):
                self.tile_map[y].append(copy.copy(
                    registries.TILE_REGISTRY.get_tile(json.load(open("maps/0_0.json"))[y][x])))

        self.tile_dim = json.load(open("properties.json"))["tile_dim"]
        self.grid_width = len(self.tile_map[0])
        self.grid_height = len(self.tile_map)
