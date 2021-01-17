#! /usr/bin/env python
from builtins import range

import sys


class TicTacToe(object):
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.player = 0

    def play(self):
        while not self._is_ended():
            self._print_board()
            try:
                user_input = input('Player {}: \n'.format(self.player + 1))
                if user_input == 'exit':
                    sys.exit()
                move = self._parse_move(user_input)
                print('You selected: {}'.format(move))
                self._make_move(move)
            except Exception as e:
                print('{}, try again...'.format(e))
                continue
            self.player = (self.player + 1) % 2

        self._print_board()
        if self._is_tie():
            print('Game tied!')
        else:
            print('Game over: congratulations Player {}'.format(
                1 if self._is_symbol_won('X') else 2
            ))

    def _print_board(self):
        print('{} | {} | {}'.format(
            self.board[6], self.board[7], self.board[8]
        ))
        print('--+---+--')
        print('{} | {} | {}'.format(
            self.board[3], self.board[4], self.board[5]
        ))
        print('--+---+--')
        print('{} | {} | {}'.format(
            self.board[0], self.board[1], self.board[2]
        ))

    def _is_ended(self):
        return (
            self._is_symbol_won('X') or
            self._is_symbol_won('O') or
            self._is_tie()
        )

    def _is_tie(self):
        return all(b == 'X' or b == 'O' for b in self.board)

    def _is_symbol_won(self, symbol):
        return (
            self._is_row_win(symbol) or
            self._is_column_win(symbol) or
            self._is_diagonal_win(symbol)
        )

    def _is_row_win(self, symbol):
        return any(
            all(
                self.board[self._coords_to_index((col, row))] == symbol
                for col in range(1, 4)
            ) for row in range(1, 4)
        )

    def _is_column_win(self, symbol):
        return any(
            all(
                self.board[self._coords_to_index((col, row))] == symbol
                for row in range(1, 4)
            ) for col in range(1, 4)
        )

    def _is_diagonal_win(self, symbol):
        d1 = all(
            self.board[self._coords_to_index((c, c))] == symbol
            for c in range(1, 4)
        )

        d2 = all(
            self.board[self._coords_to_index((4 - c, c))] == symbol
            for c in range(1, 4)
        )

        return d1 or d2

    def _parse_move(self, move):
        if len(move) != 1:
            raise 'Moves must be a square number'

        move = int(move)
        if move < 1 or move > 9:
            raise 'Square numbers are in [1, 9]'

        return move

    def _make_move(self, move):
        index = move - 1
        if self.board[index] == 'X' or self.board[index] == 'O':
            raise 'That space is already occupied'

        self.board[index] = 'X' if self.player == 0 else 'O'

    def _coords_to_index(self, coords):
        return 3 * (coords[-1] - 1) + coords[0] - 1


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.play()
