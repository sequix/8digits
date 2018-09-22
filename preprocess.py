#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import pickle
from board import Board
from reader import Reader
from queues import Queue

def calc_answers():
    '''计算所有棋盘的最短路径'''
    used = set()
    open = Queue()
    close = []
    board_first = Board(range(9))

    used.add(board_first)
    open.append(board_first)
    close.append(board_first)

    while len(open) > 0:
        board_current = open.pop()
        close.append(board_current)

        new_boards = [
            board_current.move_up(),
            board_current.move_down(),
            board_current.move_left(),
            board_current.move_right()
        ]

        for new_board in new_boards:
            if new_board and new_board not in used:
                open.push(new_board)
                used.add(new_board)

    return {x: x.reversed_path() for x in close}


def get_answers():
    '''返回所有棋盘的答案'''
    ANSWERS_CACHE = './answers.pickle'
    if os.path.exists(ANSWERS_CACHE):
        with open(ANSWERS_CACHE, 'rb') as f:
            answers = pickle.load(f)
    else:
        answers = calc_answers()
        with open(ANSWERS_CACHE, 'wb') as f:
            pickle.dump(answers, f)
    return answers
    

reader = Reader()
answers = get_answers()
while True:
    try:
        board = reader.read_board()
    except:
        break
    print(''.join(answers[board]))
