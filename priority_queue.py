#!/usr/bin/env python3
# -*- coding: utf8 -*-
# 包装heapq，实现稳定的优先队列

import heapq

class PriorityQueue:
    '''可实现稳定排序的优先队列'''
    def __init__(self, initial=None, key=lambda x:x):
        self.key = key
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.next = len(initial)
        else:
            self._data = []
            self.next = 0

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.next, item))
        self.next += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._data)
