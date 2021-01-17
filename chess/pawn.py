from chess.colors import Color
from chess.figure import AbstractChessFigure


class Pawn(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♙'
        else:
            return '♟'
        
    def can_move(self, row, col):
        if self.col != col:
            return False

        if self.color == Color.WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        
        return False