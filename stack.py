#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/12 下午1:38
# @Author: Bruce Chen
# @Site: 
# @File: stack.py
# @Software: PyCharm

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def get_top(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.get_top())
    print(s.pop())
    s.push(4)
    print(s.pop())
