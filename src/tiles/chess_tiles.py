from src.tiles.tile import Tile
from src.graphics import colors as c


class Empty(Tile):
    def __init__(self):
        self.highlighted = False
        super().__init__()


class Pawn(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_pawn.png"
        else:
            return "assets/textures/w_pawn.png"


class Bishop(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_bishop.png"
        else:
            return "assets/textures/w_bishop.png"


class Knight(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_knight.png"
        else:
            return "assets/textures/w_knight.png"


class Rook(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_rook.png"
        else:
            return "assets/textures/w_rook.png"


class Queen(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_queen.png"
        else:
            return "assets/textures/w_queen.png"


class King(Empty):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def get_image(self):
        if self.color:
            return "assets/textures/b_king.png"
        else:
            return "assets/textures/w_king.png"
