from chess.colors import Color
from chess.knight import Knight
from chess.bishop import Bishop
from chess.rook import Rook
from chess.board import Board
import pytest


def test_initial_board_size():
    board = Board()
    assert len(board.field) == board.FIELD_SIZE
    for column in board.field:
        assert len(column) == board.FIELD_SIZE
    

def test_white_first():
    board = Board()
    assert board.current_color == Color.WHITE


def test_initial_setup():
    """ начальный спавн фигур """ 
    board = Board()
    
    fig = board.field[0][0]
    assert fig.color == Color.WHITE
    assert isinstance(fig, Rook)

    fig = board.field[0][1]
    assert fig.color == Color.WHITE
    assert isinstance(fig, Knight)

    fig = board.field[0][2]
    assert fig.color == Color.WHITE
    assert isinstance(fig, Bishop)


def test_cant_move_wrong_command():
    board = Board()
    assert not board.can_move(10, 10, 0, 0)


def test_cant_move_same_place():
    board = Board()
    assert not board.can_move(0, 0, 0, 0)


def test_cant_move_no_figure():
    board = Board()
    assert not board.can_move(5, 5, 5, 5)