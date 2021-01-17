from chess.colors import Color
from chess.board import Board


def print_invitation():
    pass


def main():
    board = Board()
    board.print()

    print()
    print('LETS PLAY CHESS IN TERMINAL')
    print('===')
    print('Передвинуть фигуру: move <x1> <y1> <x2> <y2>')
    print('Выйти из игры:      exit')

    while True:
        if board.current_color == Color.WHITE:
            print('Ход белых')
        else:
            print('Ход черных')

        command = input('Введите команду: ')
        if command == 'exit':
            return

        command = command.split()
        col, row, col_new, row_new = map(int, command[1:])

        if board.can_move(row, col, row_new, col_new):
            board.move(row, col, row_new, col_new)
            board.change_color()
            board.print()


main()
