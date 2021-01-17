from chess.figure import AbstractChessFigure
from chess.colors import Color


class Knight(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♘'
        else:
            return '♞'
        
    def can_move(self, row, col):
        dx = abs(self.col - col)
        dy = abs(self.row - row)
        if abs(dx*dy) == 2:
            return True
        else:
            return False
