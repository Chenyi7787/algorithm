#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/5 下午3:40
# @Author: Bruce Chen
# @Site: 
# @File: leetcode_350.py
# @Software: PyCharm

import sys
sys.path.append("../")
from calc_time_decorator import calc_time

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]


说明：

    输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    我们可以不考虑输出结果的顺序。

进阶：

    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from collections import Counter

class Solution_1:
    def _intersect(self, nums1, nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: list[int]
        """
        if len(nums1) > len(nums2):
            self._intersect(nums2, nums1)
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        result = []
        for key in dic1:
            if key in dic2:
                i = min(dic1[key], dic2[key])
                while i > 0:
                    result.append(key)
                    i -= 1
        return result

    @calc_time
    def intersect(self, nums1, nums2):
        return self._intersect(nums1, nums2)


class Solution_2:
    def _intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            self._intersect(nums2, nums1)
        m = Counter()
        for num in nums1:
            m[num] += 1
        result = []
        for num in nums2:
            if m.get(num, 0) > 0:
                result.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        return result

    @calc_time
    def intersect(self, nums1, nums2):
        return self._intersect(nums1, nums2)


class Solution_3:
    @calc_time
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        result = list()
        i, j = 0, 0
        while i < length1 and j < length2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    test1 = Solution_1()
    result1 = test1.intersect(nums1, nums2)
    print(result1)
    test2 = Solution_2()
    result2 = test2.intersect(nums1, nums2)
    print(result2)
    test3 = Solution_3()
    result3 = test3.intersect(nums1, nums2)
    print(result3)

