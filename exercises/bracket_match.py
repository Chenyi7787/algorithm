#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/12 下午4:18
# @Author: Bruce Chen
# @Site: 
# @File: bracket_match.py
# @Software: PyCharm

"""
{[()]}
"""
import sys
sys.path.append("../")
from data_structure.stack import Stack

class Solution:
    def bracket_match(self, s):
        """
        :param s: str
        :return: bool
        """
        dic = {')':'(', '}':'{', ']':'['}
        stack = Stack()
        for i in s:
            if i in {'{', '[', '('}:
                stack.push(i)
            else:
                if stack.get_top() == dic[i]:
                    stack.pop()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False


if __name__ == "__main__":
    s = "{[()()]}"
    test = Solution()
    result = test.bracket_match(s)
    print(result)



