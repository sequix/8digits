#!/usr/bin/env python3
# -*- coding: utf8 -*-
# 生成所有棋盘和对应序号相互转换的表

import itertools

first_board = tuple(range(9))
serial2board = itertools.permutations(first_board)
board2serial = {}

for serial, board in enumerate(serial2board):
    board2serial[board] = serial
