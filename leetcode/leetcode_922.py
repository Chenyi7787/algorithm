#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/6 下午2:48
# @Author: Bruce Chen
# @Site: 
# @File: leetcode_922.py
# @Software: PyCharm

"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

提示：

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""
class Solution_1:
    def sortArrayByParity(self, A):
        """
        :param A: list[int]
        :return: list[int]
        """
        odd_list = []
        even_list = []
        result = []
        for num in A:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even_list.pop())
            else:
                result.append(odd_list.pop())
        return result

class Solution_2:
    def sortArrayByParity(self, A):
        i, j = 0, 1
        while j <= (len(A)-1) and i <= (len(A)-1):
            if A[i] % 2 == 1:
                if A[j] % 2 == 1:
                    j += 2
                else:
                    A[i], A[j] = A[j], A[i]
            else:
                i += 2
        return A

class Solution_3:
    def sortArrayByParity(self, A):
        result = [0 for i in range(len(A))]
        i = 0
        j = 1
        for num in A:
            if num % 2 == 0:
                result[i] = num
                i += 2
        for num in A:
            if num % 2 == 1:
                result[j] = num
                j += 2
        return result



if __name__ == "__main__":
    A = [4,2,5,7,6,9,8,3]
    test1 = Solution_1()
    result1 = test1.sortArrayByParity(A)
    print(result1)
    test2 = Solution_2()
    result2 = test2.sortArrayByParity(A)
    print(result2)
    test3 = Solution_3()
    result3 = test3.sortArrayByParity(A)
    print(result3)