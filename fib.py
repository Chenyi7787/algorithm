class Solution:
    def fib(self, n):
        '''
        :param n: int
        :return: int
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return self.fib(n-2) + self.fib(n-1)


if __name__ == "__main__":
    test = Solution()
    print(test.fib(2))
