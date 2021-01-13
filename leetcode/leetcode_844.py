#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/13 上午11:19
# @Author: Bruce Chen
# @Site: 
# @File: leetcode_844.py.py
# @Software: PyCharm

"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

提示：

    1 <= S.length <= 200
    1 <= T.length <= 200
    S 和 T 只含有小写字母以及字符 '#'。

进阶：

    你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""

class Solution_1:
    def backspaceCompare(self, S, T):
        """
        :param S: str
        :param T: str
        :return: bool
        """
        stack1 = []
        stack2 = []
        for i in S:
            if len(stack1) != 0:
                if i == '#':
                    stack1.pop()
                else:
                    stack1.append(i)
            else:
                if i == '#':
                    continue
                else:
                    stack1.append(i)
        for j in T:
            if len(stack2) != 0:
                if j == '#':
                    stack2.pop()
                else:
                    stack2.append(j)
            else:
                if j == '#':
                    continue
                else:
                    stack2.append(j)
        print(stack1, stack2)
        if stack1 == stack2:
            return True
        else:
            return False


class Solution_2:
    def backspaceCompare(self, S, T):
        i, j = len(S)-1, len(T)-1
        skipS, skipT = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1
        return True








if __name__ == "__main__":
    S = "e#####"
    T = "g###"
    test = Solution_1()
    result = test.backspaceCompare(S, T)
    print(result)