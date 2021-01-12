#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/8 下午3:46
# @Author: Bruce Chen
# @Site: 
# @File: binary_search.py
# @Software: PyCharm

# li = [4, 2, 6, 8, 3, 1, 5, 9, 7]

# recursive solution
def binary_sort_1(li, left, right, val):
    if left > right:
        return None
    mid = (left + right) // 2
    if li[mid] == val:
        return mid
    elif li[mid] > val:
        right = mid - 1
    else:
        left = mid + 1
    return binary_sort_1(li, left, right, val)


# non-recursive solution
def binary_sort_2(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None



if __name__ == "__main__":
    li = [1,2,3,4,5,6,7,8,9]
    result = binary_sort_2(li, 6)
    print(result)