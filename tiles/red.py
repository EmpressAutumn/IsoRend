import main


RED = (255, 0, 0)
BLUE = (0, 0, 255)


class RedBlue(main.Tile):
    def __init__(self):
        self._clicked = False
        super().__init__()

    def get_color(self):
        if self._clicked:
            return RED
        else:
            return BLUE

    def click(self):
        self._clicked = not self._clicked
