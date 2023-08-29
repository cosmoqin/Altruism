class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # https://leetcode.cn/problems/unique-paths
        # 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
        # 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
        # 问总共有多少条不同的路径？

        # 状态转移方程 f(i,j) = f(i-1,j) + f(i,j-1) 但 dp[0][j],dp[i][0] = 1
        # 因为只往右下，所以这些值不会被renew

        dp = [[1] * n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1,n-1]



return dp[m][n]
