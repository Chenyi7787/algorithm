# coding=utf-8
# author by Bruce Chen 2020/12/18
import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print("{} run time: {}s".format(func.__name__, end-start))
        return value
    return wrapper