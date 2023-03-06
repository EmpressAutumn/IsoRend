from src.tiles import tile, red


class Registry:  # Dynamic Tile Registry
    def __init__(self):
        self._registrar = {}

    def register(self, key, tile):
        self._registrar.update({key: tile})

    def get_tile(self, key):
        return self._registrar[key]


TILE_REGISTRY = Registry()


def register_all():
    TILE_REGISTRY.register("0", tile.Tile())
    TILE_REGISTRY.register("red", red.RedBlue())
