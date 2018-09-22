#!/usr/bin/env python3
# -*- coding: utf8 -*-

from utils import board2serial

class Board:
    '''8数码棋盘 (immutable)'''
    def __init__(self, board=None, path=None):
        self.board = board or (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.board = tuple(self.board)
        self.path = path or ()
        self.path = tuple(self.path)
        self.zi = self.board.index(0)
        self.zx = self.zi // 3
        self.zy = self.zi % 3
        self.priority = len(self.path) + self.zx + self.zy

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

    def reversed_path(self):
        '''返回取反的路径'''
        reversed_movement = {'u':'d', 'd':'u', 'l':'r', 'r':'l'}
        reversed_path = reversed(self.path)
        reversed_path = tuple(map(lambda x: reversed_movement[x], reversed_path))
        return reversed_path

    def __eq__(self, other):
        '''仅比较棋盘，不比较路径'''
        return self.board == other.board

    def __hash__(self):
        '''以全排列中的序号作为hash值'''
        return board2serial[self.board]
