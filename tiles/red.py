import main


RED = (255, 0, 0)
BLUE = (0, 0, 255)


class RedBlue(main.Tile):
    def __init__(self):
        self._clicked = False
        super().__init__(BLUE)

    def click(self):
        print("Clicked on a RedBlue tile")
        self._clicked = not self._clicked
        if self._clicked:
            self._color = RED
        else:
            self._color = BLUE
