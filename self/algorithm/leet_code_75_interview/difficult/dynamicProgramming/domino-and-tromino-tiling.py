class Solution:
    def numTilings(self, n: int) -> int:
        """
        有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
        给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 109 + 7 取模 的值。
        平铺指的是每个正方形都必须有瓷砖覆盖。
        两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。
        https://leetcode.cn/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75
        """
        mod = 10**9+7
        # 模拟当前一列是已填满，如果填充下一列
        # 下一列有四种状态，全空，下空，上空，全满
        # 1.rlt[i][0] = rlt[i-1][3]
        # 2.rlt[i][1] = rlt[i-1][0] + rlt[i-1][1]
        # 3.rlt[i][2] = rlt[i-1][0] + rlt[i-1][2]
        # 4.rlt[i][3] = rlt[i-1][0] + rlt[i-1][1] + rlt[i-1][2] + rlt[i-1][3]
        rlt = [[0]*4 for _ in range(n+1)]
        rlt[0][3] = 1
        for i in range(1,n+1):
            rlt[i][0] = (rlt[i-1][3]) % mod
            rlt[i][1] = (rlt[i-1][0] + rlt[i-1][1]) % mod
            rlt[i][2] = (rlt[i-1][0] + rlt[i-1][2]) % mod
            rlt[i][3] = (rlt[i-1][0] + rlt[i-1][1] + rlt[i-1][2] + rlt[i-1][3]) % mod

        return rlt[n][3]
        # statList = [0] * (n+1)
        # for i in range(0,n+1):
        #     if i ==0:
        #         statList[i] = 1
        #     elif i == 1:
        #         statList[i] = 1
        #     elif i == 2:
        #         statList[i] = statList[i-1] + statList[i-2]
        #     else:
        #         statList[i] = statList[i-1] + statList[i-2] + 2*statList[i-3]
        # return statList[n] % (10**9 + 7)