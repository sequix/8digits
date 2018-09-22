#!/usr/bin/env python3
# -*- coding: utf8 -*-
# 也可使用python的queue模块中提供的Queue和PriorityQueue，
# 只不过他们是多线程场景下使用个队列，大材小用

import heapq

class Queue(list):
    '''队列'''
    def push(self, item):
        self.append(item)

    def pop(self):
        return super().pop(0)


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

    def __len__(self):
        return len(self._data)
