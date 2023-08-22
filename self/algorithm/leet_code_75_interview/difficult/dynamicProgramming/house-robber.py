class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。
        每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
        给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
        https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75
        """

        '''
        同样动态规划的思路
        '''
        n = len(nums)
        statList = [0]*n
        for i in range(0,n):
            if i == 0:
                statList[i] = nums[0]
            elif i == 1:
                statList[i] = nums[1] #不能偷0
            else :
                statList[i] = max(statList[i-2]+nums[i],statList[i-1]) # option.1 不偷当前房子 option.2 偷当前房子 但上一个房子不可以偷
        return statList[n-1]