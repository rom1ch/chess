from chess.board import Board
from chess.rook import Rook
from chess.colors import Color


def test_can_move():
    board = Board()
    rook = Rook(4, 4, Color.WHITE, board)
    assert rook.can_move(4, 6)


def test_cant_move_diagonal():
    board = Board()
    rook = Rook(0, 0, Color.WHITE, board)
    assert not rook.can_move(1, 1)


def test_cant_move_with_obstacles():
    board = Board()
    rook = Rook(7, 0, Color.BLACK, board)
    assert not rook.can_move(4, 0)


def test_icon():
    board = Board()
    
    rook = Rook(0, 0, Color.WHITE, board)
    assert rook.char() == '♖'
    
    rook = Rook(0, 0, Color.BLACK, board)
    assert rook.char() == '♜'