class Solution:
    def tribonacci(self, n: int) -> int:
        """
        1137. 第 N 个泰波那契数
        泰波那契序列 Tn 定义如下： 
        T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
        给你整数 n 请返回第 n 个泰波那契数 Tn 的值。
        
        https://leetcode.cn/problems/n-th-tribonacci-number/
        """

        """
        理解Dynamic programming - 
        1.状态定义 - 将对应的状态转到数组里
        2.状态转移 - 数组存值
        """
        tribonacciList = [0]*(n+1)
        for i in range(0,n+1):
            if i == 0:
                tribonacciList[0] = 0
            elif i == 1:
                tribonacciList[1] = 1
            elif i == 2:
                tribonacciList[2] = 1
            else:
                tribonacciList[i] = tribonacciList[i-3] + tribonacciList[i-2] + tribonacciList[i-1]
        return tribonacciList[n]
        # @lru_cache
        # def fibonacci(n):
        #     if n == 0:
        #         return 0
        #     elif n==1:
        #         return 1
        #     elif n==2:
        #         return 1
        #     else:
        #         return fibonacci(n-2) + fibonacci(n-1) + fibonacci(n-3)
        # return fibonacci(n)
