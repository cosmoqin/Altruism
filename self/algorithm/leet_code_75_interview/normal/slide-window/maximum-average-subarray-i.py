class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
        请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
        任何误差小于 10-5 的答案都将被视为正确答案。
        """
        nums =[0,1,1,3,3]
        k=4
        n = len(nums)
        maxavg = sum(nums[0:k])/k
        for i in range(k,n):
            maxavg = max(maxavg,(maxavg*k + nums[i] - nums[i-k])/k)
        return maxavg