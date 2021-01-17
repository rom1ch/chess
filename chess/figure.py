class AbstractChessFigure:
    """ Базовый класс для всех шахматных фигур """

    def __init__(self, row: int, col: int, color: int, board) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.board = board

    def char(self):
        return None
    
    def can_move(self, row, col):
        return True
    