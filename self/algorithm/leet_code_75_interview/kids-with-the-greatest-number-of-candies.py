class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/
        
        '''
        maxCandies = 0
        candiesLen = len(candies)
        i = 0
        while i < candiesLen:
            maxCandies = maxCandies if maxCandies >= candies[i] else candies[i]
            i += 1
        asseartList = []
        for i in candies:
            if i + extraCandies < maxCandies:
                asseartList.append(False)
            else:
                asseartList.append(True)
        return asseartList
        # optimization
        return list(map(lambda s:candies[s]+extraCandies >= max(candies) ,candies))
