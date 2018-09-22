#!/usr/bin/env python3
# -*- coding: utf8 -*-
# 生成所有棋盘和对应序号相互转换的表

import os
import pickle
import itertools

# 序号 和 局面的转换表的缓存文件名
SERIAL2BOARD_CACHE = './serial2board.pickle'
BOARD2SERIAL_CACHE = './board2serial.pickle'

# 序号 和 局面的转换表
serial2board = None
board2serial = None


def get_serial2board():
    '''返回序号到局面的转换表'''
    global serial2board

    if serial2board is not None:
        return serial2board

    if os.path.exists(SERIAL2BOARD_CACHE):
        with open(SERIAL2BOARD_CACHE, 'rb') as f:
            serial2board = pickle.load(f)
        return serial2board

    first_board = list(range(9))
    serial2board = list(itertools.permutations(first_board))

    with open(SERIAL2BOARD_CACHE, 'wb') as f:
        pickle.dump(serial2board, f)
    return serial2board


def get_board2serial():
    '''返回局面到序号的转换表'''
    global board2serial

    if board2serial is not None:
        return board2serial

    if os.path.exists(BOARD2SERIAL_CACHE):
        with open(BOARD2SERIAL_CACHE, 'rb') as f:
            board2serial = pickle.load(f)
        return board2serial

    serial2board = get_serial2board()
    board2serial = {}

    for serial, board in enumerate(serial2board):
        board2serial[board] = serial

    with open(BOARD2SERIAL_CACHE, 'wb') as f:
        pickle.dump(board2serial, f)
    return board2serial


if __name__ != '__main__':
    get_serial2board()
    get_board2serial()
