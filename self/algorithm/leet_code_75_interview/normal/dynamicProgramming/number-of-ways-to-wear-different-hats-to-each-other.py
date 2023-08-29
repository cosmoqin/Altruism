class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """
        总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。
        给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。
        请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。
        由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。
        https://leetcode.cn/problems/number-of-ways-to-wear-different-hats-to-each-other

        提示：
        n == hats.length
        1 <= n <= 10
        1 <= hats[i].length <= 40
        1 <= hats[i][j] <= 40
        hats[i] 包含一个数字互不相同的整数列表。

        from July 30th 21:50
        """

        '''
        先算全部 n * n-1...
        再减， 第一个重复的 第二个重复的
        '''
        '''
        第一个方法 - 写一个递归 每次传入选定一个帽子后的list. 读题 + 写个递归 28min 
        '''
        hats = [[3,4],[4,5],[5]]
        import math
        solutionNums = 0
        removeHat = {0}
        def getHatsNumbers(solutionNums,removeHat,hats: List[List[int]]) -> int:
            hatsList = hats[0]
            hatSet = set(hatsList)
            for i in removeHat:
                if i in hatSet:
                    hatSet.remove(i)
                
            hatsList = list(hatSet)
            # 这个人没想要的帽子
            if len(hatsList) == 0 :
                return solutionNums 
            # 有想要的帽子 且是最后一个人 
            elif len(hats) == 1:
                solutionNums = solutionNums + hats[0]
                return solutionNums
            # 随便选一顶帽子 递归到最后一个人或第一个没想要的帽子的人停止
            else:
                for hatIdex in range(0,len(hatsList)):
                    removeHat.append(hatsList[hatIdex])
                    return getHatsNumbers(solutionNums,removeHat,hats.remove(hatsList))
        return getHatsNumbers(solutionNums,removeHat,hats) % (math.pow(10,9) + 7)
                


hats = [[3,4],[4,5],[5]]
import math
solutionNums = 0
removeHat = {0}
def getHatsNumbers(solutionNums,removeHat,hats):
    hatsList = hats[0]
    hatSet = set(hatsList)
    for i in removeHat:
        if i in hatSet:
            hatSet.remove(i)
        
    hatsList = list(hatSet)
    # 这个人没想要的帽子
    if len(hatsList) == 0 :
        return solutionNums 
    # 有想要的帽子 且是最后一个人 
    elif len(hats) == 1:
        solutionNums = solutionNums + len(hats[0])
        return solutionNums
    # 随便选一顶帽子 递归到最后一个人或第一个没想要的帽子的人停止
    else:
        for hatIdex in range(0,len(hatsList)):
            print(hatIdex)
            removeHatTmp = removeHat
            removeHatTmp.add(hatsList[hatIdex])
            hatsTemp = hats
            print(removeHatTmp)
            print(solutionNums,removeHat,hats)
            return getHatsNumbers(solutionNums,removeHatTmp,hatsTemp.remove(hats[0]))


getHatsNumbers(solutionNums,removeHat,hats) 
% (math.pow(10,9) + 7)

# 动态规划 状态转移
import math

# if __name__ == "__main__":
inf = 1 << 31
# 邻接矩阵存储边权重
d = [[inf for _ in range(10)] for _ in range(10)]
# 测试数据
edges = [[0, 1, 3], [1, 2, 5], [2, 3, 5], [3, 4, 3], [4, 0, 7], [4, 1, 6], [0, 3, 4], [2, 0, 4]]
for u, v, l in edges:
    d[u][v] = l
# 初始化成近似无穷大的值
dp = [[inf for _ in range(5)] for _ in range((1 << 5))]
dp[0][0] = 0
# 遍历状态
for s in range(1, (1 << 5)):
    for u in range(5):
        # 遍历决策
        for v in range(5):
            # 必须要求这个点没有去过
            if (s >> v) & 1 == 0:
                continue
            dp[s][v] = min(dp[s][v], dp[s - (1 << v)][u] + d[u][v])


print(dp[(1 << 5) - 1][0])