class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        746. 使用最小花费爬楼梯
        给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
        一旦你支付此费用，即可选择向上爬一个或者两个台阶。
        你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
        请你计算并返回达到楼梯顶部的最低花费。
        https://leetcode.cn/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=leetcode-75
        """

        '''
        1.状态定义
        2.状态转移方程

        '''
        n = len(cost)
        statList = [0] * (n+1) # 用于存走到每一步台阶所需要的最小费用
        for i in range(0,n+1):
            if i == 0:
                statList[0] = 0
            elif i == 1:
                statList[1] = 0
            else:
                statList[i] = min(statList[i-1]+cost[i-1] , statList[i-2]+cost[i-2]) #退一格和退两格
        return statList[n]
        '''
        优化的点：
        因为 i 只和 i-1 i-2有关 其实只需要两个变量存 i-1,i-2的值 可以减少空间复杂度至O(1)
        '''