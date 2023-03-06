from src.tiles import tile, red
from src.tiles import chess_tiles as ct


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
    TILE_REGISTRY.register("e", ct.Empty())
    TILE_REGISTRY.register("wp", ct.Pawn(False))
    TILE_REGISTRY.register("wb", ct.Bishop(False))
    TILE_REGISTRY.register("wn", ct.Knight(False))
    TILE_REGISTRY.register("wr", ct.Rook(False))
    TILE_REGISTRY.register("wq", ct.Queen(False))
    TILE_REGISTRY.register("wk", ct.King(False))
    TILE_REGISTRY.register("bp", ct.Pawn(True))
    TILE_REGISTRY.register("bb", ct.Bishop(True))
    TILE_REGISTRY.register("bn", ct.Knight(True))
    TILE_REGISTRY.register("br", ct.Rook(True))
    TILE_REGISTRY.register("bq", ct.Queen(True))
    TILE_REGISTRY.register("bk", ct.King(True))
