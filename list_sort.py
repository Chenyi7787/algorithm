# coding=utf-8
# author by Bruce Chen 2020/12/18
import random
from calc_time_decorator import calc_time

@calc_time
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


@calc_time
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

@calc_time
def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

# quick_sort
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@calc_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)


# heap_sort
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j+1 <= high and li[j] > li[j+1]:
            j = j + 1
        if li[j] < tmp:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_sort(li):
    # create heap
    n = len(li)
    last_par_node = (n-2) // 2
    while last_par_node >=0:
        sift(li, last_par_node, n-1)
        last_par_node -= 1

    # heap sort
    last_node = n - 1
    while last_node >= 0:
        li[last_node], li[0] = li[0], li[last_node]
        sift(li, 0, last_node-1)
        last_node -= 1

# topk_1
@calc_time
def topk_1(li, k):
    heap = li[0:k]
    # create heap
    last_par_node = (k-2) // 2
    while last_par_node >= 0:
        sift(heap, last_par_node, k-1)
        last_par_node -= 1
    # traverse list
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # heap sort
    n = k - 1
    while n >= 0:
        heap[n], heap[0] = heap[0], heap[n]
        sift(heap, 0, n-1)
        n -= 1
    return heap

# topk_2
@calc_time
def topk_2(li, k):
    for i in range(k):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li[-1:-(k+1):-1]




li = list(range(100000000))
random.shuffle(li)

# li = [5,4,2,7,1,3,9,8,6]
# li = [4,7,0,9,1,5,3,3,2,6]
# bubble_sort(li)
# select_sort(li)
#quick_sort(li)
#heap_sort(li)
print(topk_1(li, 10))
print(topk_2(li, 10))
#print(li)
# li2 = topk(li, 10)
# print(li2)
# heap_sort(li2)
# print(li2)




