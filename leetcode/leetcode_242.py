# coding=utf-8
# author by Bruce Chen 2021/01/04

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true

示例 2:

输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''

# Solution_1
class Solution_1:
    def isanagram(self, s, t):
        '''
        :param s: str
        :param t: str
        :return: bool
        '''
        # 1. len(s) != len(t), return False
        # 2. len(s) == len(t) == 0, return True
        # 3. len(s) == len(t) != 0, counter(s) ?= counter(t)

        if len(s) != len(t):
            return False
        else:
            if len(s) == 0:
                return True
            dic1 = {}
            for i in s:
                if i not in t:
                    return False
                else:
                    if i not in dic1:
                        dic1[i] = 1
                    else:
                        dic1[i] += 1
            dic2 = {}
            for j in t:
                if j not in s:
                    return False
                else:
                    if j not in dic2:
                        dic2[j] = 1
                    else:
                        dic2[j] += 1
            if dic2 == dic1:
                return True
            else:
                return False


# Solution_2
class Solution_2:
    def isanagram(self, s, t):
        '''
        :param s: str
        :param t: str
        :return: bool
        '''
        # ideas: sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)


# Solution_3
from collections import Counter
class Solution_3:
    def isanagram(self, s, t):
        '''
        :param s: str
        :param t: str
        :return: bool
        '''
        # ideas: Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        else:
            return Counter(s) == Counter(t)



if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    test = Solution_3()
    result = test.isanagram(s, t)
    print(result)
