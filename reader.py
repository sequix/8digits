#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re
import sys
from board import Board

class Reader():
    '''以空白符(\t\r\n)分隔的字符串为单位的stdin解析器'''
    def __init__(self):
        self.buffer = []
        self.splitter = re.compile(r'[ \t\r\n]+')

    def fill_buffer(self):
        self.buffer.extend(self.splitter.split(input()))
        
    def read_int(self):
        if len(self.buffer) == 0:
            self.fill_buffer()
        word = self.buffer.pop(0)
        return int(word)

    def read_board(self):
        board = []
        for i in range(9):
            board.append(self.read_int())
        return Board(board)
