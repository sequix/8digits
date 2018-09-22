#!/usr/bin/env python3
# -*- coding: utf8 -*-

from board import Board
from reader import Reader
from queues import Queue

used = set()
que = Queue()
reader = Reader()
board_goal = Board(range(9))

initial_board = reader.read_board()
used.add(initial_board)
que.push(initial_board)

while len(que) > 0:
    board_current = que.pop()

    if board_current == board_goal:
        board_goal = board_current
        break

    new_boards = [
        board_current.move_up(),
        board_current.move_down(),
        board_current.move_left(),
        board_current.move_right()
    ]

    for new_board in new_boards:
        if new_board and new_board not in used:
            que.push(new_board)
            used.add(new_board)

print(''.join(board_goal.path))
