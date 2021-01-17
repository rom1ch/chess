from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.knight import Knight
from chess.colors import Color
from chess.bishop import Bishop
from chess.rook import Rook


class Board:
    """ ASCII шахматы """

    FIELD_SIZE = 8
    
    def __init__(self) -> None:
        self.field = []
        self.current_color = Color.WHITE
        for i in range(self.FIELD_SIZE):
            self.field.append([None] * self.FIELD_SIZE)
        
        # стандартная расстановка
        self.field[0] = [
            Rook(  0, 0, Color.WHITE, self), 
            Knight(0, 1, Color.WHITE, self),
            Bishop(0, 2, Color.WHITE, self),
            Queen( 0, 3, Color.WHITE, self),
            King(  0, 4, Color.WHITE, self),
            Bishop(0, 5, Color.WHITE, self), 
            Knight(0, 6, Color.WHITE, self), 
            Rook(  0, 7, Color.WHITE, self),
        ]

        self.field[1] = [
            Pawn(1, 0, Color.WHITE, self),
            Pawn(1, 1, Color.WHITE, self),
            Pawn(1, 2, Color.WHITE, self),
            Pawn(1, 3, Color.WHITE, self),
            Pawn(1, 4, Color.WHITE, self),
            Pawn(1, 5, Color.WHITE, self),
            Pawn(1, 6, Color.WHITE, self),
            Pawn(1, 7, Color.WHITE, self),
        ]

        self.field[6] = [
            Pawn(6, 0, Color.BLACK, self),
            Pawn(6, 1, Color.BLACK, self),
            Pawn(6, 2, Color.BLACK, self),
            Pawn(6, 3, Color.BLACK, self),
            Pawn(6, 4, Color.BLACK, self),
            Pawn(6, 5, Color.BLACK, self),
            Pawn(6, 6, Color.BLACK, self),
            Pawn(6, 7, Color.BLACK, self),
        ]
        
        self.field[7] = [
            Rook(  7, 0, Color.BLACK, self), 
            Knight(7, 1, Color.BLACK, self), 
            Bishop(7, 2, Color.BLACK, self),
            Queen( 7, 3, Color.BLACK, self),
            King(  7, 4, Color.BLACK, self),
            Bishop(7, 5, Color.BLACK, self), 
            Knight(7, 6, Color.BLACK, self), 
            Rook(  7, 7, Color.BLACK, self),
        ]

        # TODO кастомная расстановка как необязательный параметр

    def print(self):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', self.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='       ')
        for col in range(8):
            print(col, end='    ')
        print()

    def cell(self, row: int, col: int) -> str:
        """ Возвращает строку с изображением фигуры 
        
        Если фигуры в клетке нет, то ''.
        Если фигура есть, то цвет+иконка, например wP.
        """
        piece = self.field[row][col]
        if piece:
            return piece.char() + ' '
        else:
            return '  '

    def can_move(self, row: int, col: int, row_new: int, col_new: int):
        """ Проверить, можно ли сходить [row][col] -> [row_new][col_new] """
        
        # некорректная команда от игрока
        if not (0 <= col < self.FIELD_SIZE and 0 <= row < self.FIELD_SIZE and 0 <= col_new < self.FIELD_SIZE and 0 <= row_new < self.FIELD_SIZE):
            return False
        if row == row_new and col == col_new:
            return False
        
        figure_from = self.field[row][col]
        figure_to = self.field[row_new][col_new]
        
        # нельзя сходить, если нет фигуры
        if figure_from is None:
            return False

        # нельзя ходить чужими фигурами
        if figure_from.color != self.current_color:
            return False

        # проверка, что теоретически фигура может туда попасть
        if figure_from.can_move(row_new, col_new):
            return True
        
        # нельзя сходить в свою уже занятую клетку
        if figure_from.color == figure_to.color:
            return False
        
    def change_color(self):
        if self.current_color == Color.WHITE:
            self.current_color = Color.BLACK
        else:
            self.current_color = Color.WHITE
    
    def move(self, row, col, row_new, col_new):
        """ Переместить фигуру из клетки """
        # переставляем фигуры местами
        piece = self.field[row][col]
        self.field[row][col] = None
        self.field[row_new][col_new] = piece
        piece.row = row_new
        piece.col = col_new
