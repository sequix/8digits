#!/usr/bin/env python3
# -*- coding: utf8 -*-

from collections import Iterable
from utils import board2serial, serial2board

class Board:
    '''8数码棋盘 (immutable)'''
    def __init__(self, board=None, path=None):
        self.board = board
        self.path = path or ()
        self.path = tuple(self.path)
        self.zi = self.board.index(0)
        self.zx = self.zi // 3
        self.zy = self.zi % 3
        self.priority = len(self.path) + self.zx + self.zy

    @property
    def board(self):
        return serial2board[self._board_serial]

    @board.setter
    def board(self, value):
        if isinstance(value, (list, tuple)):
            self._board_serial = board2serial[tuple(value)]
        elif isinstance(value, int):
            self._board_serial = value
        else:
            raise ValueError('expected a integer, a list or a tuple')

    def move_up(self):
        '''返回棋盘向上后的新棋盘，无法移动返回None'''
        if self.zx + 1 > 2:
            return None
        old_zi = self.zi
        new_zi = (self.zx + 1) * 3 + self.zy
        new_board = list(self.board)
        new_board[old_zi], new_board[new_zi] = new_board[new_zi], new_board[old_zi]
        new_board = tuple(new_board)
        new_path = tuple(list(self.path) + ['u'])
        return Board(new_board, new_path)

    def move_down(self):
        '''返回棋盘向下后的新棋盘，无法移动返回None'''
        if self.zx - 1 < 0:
            return None
        old_zi = self.zi
        new_zi = (self.zx - 1) * 3 + self.zy
        new_board = list(self.board)
        new_board[old_zi], new_board[new_zi] = new_board[new_zi], new_board[old_zi]
        new_board = tuple(new_board)
        new_path = tuple(list(self.path) + ['d'])
        return Board(new_board, new_path)

    def move_left(self):
        '''返回棋盘向左后的新棋盘，无法移动返回None'''
        if self.zy + 1 > 2:
            return None
        old_zi = self.zi
        new_zi = self.zx * 3 + (self.zy + 1)
        new_board = list(self.board)
        new_board[old_zi], new_board[new_zi] = new_board[new_zi], new_board[old_zi]
        new_board = tuple(new_board)
        new_path = tuple(list(self.path) + ['l'])
        return Board(new_board, new_path)

    def move_right(self):
        '''返回棋盘向右后的新棋盘，无法移动返回None'''
        if self.zy - 1 < 0:
            return None
        old_zi = self.zi
        new_zi = self.zx * 3 + (self.zy - 1)
        new_board = list(self.board)
        new_board[old_zi], new_board[new_zi] = new_board[new_zi], new_board[old_zi]
        new_board = tuple(new_board)
        new_path = tuple(list(self.path) + ['r'])
        return Board(new_board, new_path)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return board2serial[self.board]
