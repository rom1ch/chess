class AbstractChessFigure:
    """ Базовый класс для всех шахматных фигур """

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return None
    
    def can_move(self, row, col):
        return True
    