#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/12 下午2:10
# @Author: Bruce Chen
# @Site: 
# @File: queue.py
# @Software: PyCharm

class Queue(object):
    def __init__(self, size):
        self.queue = [0 for i in range(size)]
        self.rear = 0
        self.front = 0
        self.size = size

    def append(self, element):
        if not self.is_filled():
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.size
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return data
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


if __name__ == "__main__":
    q = Queue(6)
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
    #q.append(6)

    #print(q.pop())