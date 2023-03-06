from src.tiles.tile import Tile
from src.img import colors as c


class RedBlue(Tile):
    def __init__(self):
        self._clicked = False
        super().__init__(c.BLUE)

    def click(self):
        print("Clicked on a RedBlue tile")
        self._clicked = not self._clicked
        if self._clicked:
            self._color = c.RED
        else:
            self._color = c.BLUE
