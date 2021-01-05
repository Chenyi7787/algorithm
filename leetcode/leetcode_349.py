#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/4 下午6:11
# @Author: Bruce Chen
# @Site: 
# @File: leetcode_349.py
# @Software: PyCharm

import sys
sys.path.append("../")
from calc_time_decorator import calc_time

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]


说明：

    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。
"""
class Solution_1:
    @calc_time
    def intersection(self, nums1, nums2):
        '''
        :param nums1: list[int]
        :param nums2: list[int]
        :return: list[int]
        '''
        result = []
        if len(nums1) <= len(nums2):
            for i in nums1:
                if i in nums2 and i not in result:
                    result.append(i)
        else:
            for j in nums2:
                if j in nums1 and j not in result:
                    result.append(j)
        return result


class Solution_2:
    @calc_time
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return self._section(set1, set2)

    def _section(self, set1, set2):
        if len(set1) > len(set2):
            self._section(set2, set1)
        return [x for x in set1 if x in set2]

class Solution_3:
    @calc_time
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        result = list()
        i, j = 0, 0
        while i < length1 and j < length2:
            if nums1[i] == nums2[j]:
                if not result or nums1[i] != result[-1]:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    test1 = Solution_1()
    result1 = test1.intersection(nums1, nums2)
    print(result1)
    test2 = Solution_2()
    result2 = test2.intersection(nums1, nums2)
    print(result2)
    test3 = Solution_3()
    result3 = test3.intersection(nums1, nums2)
    print(result3)