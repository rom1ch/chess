from chess.colors import Color
from chess.figure import AbstractChessFigure


class Rook(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♖'
        else:
            return '♜'
        
    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        
        # выясняем направление (вверх или вниз)
        step = 1 if (row >= self.row) else -1
        # если на пути по вертикали есть фигура
        for r in range(self.row + step, row, step):
            if self.board.field[r][self.col]:
                return False

        # выясняем направление (влево или вправо)
        step = 1 if (col >= self.col) else -1
        # если на пути по горизонтали есть фигура
        for c in range(self.col + step, col, step):
            if self.board.field[self.row][c]:
                return False

        return True