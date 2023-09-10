class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。
        说明：你不能倾斜容器。
        """
        # 输入：[1,8,6,2,5,4,8,3,7]
        # 输出：49 
        # 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

        # 感觉可以用动态规划的思想来写 试一下
        # n = len(height)
        # dynamic_matrix = [0] * n
        # for i in range(0,n-1):
        #     dynamic_matrix[i] = max(dynamic_matrix[i-1],'''好像不是一维动态规划能做的''')

        # 双指针试试   
        # 至少是需要一边循环的
        # 双指针的策略是看怎么移动这些指针
        height = [1,8,6,2,5,4,8,3,7]
        n = len(height)
        pointx = 0
        pointy = n-1
        coverage = min(height[pointx],height[pointy]) * (pointy - pointx)
        while pointx < pointy:
            if height[pointx] < height[pointy]:
                pointx +=1
                coverage = max(coverage,min(height[pointx],height[pointy]) * (pointy - pointx))
                print(coverage)
            else:
                pointy -=1
                coverage = max(coverage,min(height[pointx],height[pointy]) * (pointy - pointx))
        return coverage