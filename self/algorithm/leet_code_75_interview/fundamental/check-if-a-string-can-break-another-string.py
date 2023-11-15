class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """
        给你两个字符串 s1 和 s2 ，它们长度相等，请你检查是否存在一个 s1  的排列可以打破 s2 的一个排列，或者是否存在一个 s2 的排列可以打破 s1 的一个排列。
        字符串 x 可以打破字符串 y  (两者长度都为 n ）需满足对于所有 i (在 0 到 n - 1 之间）都有 x[i] >= y[i] (字典序意义下的顺序）。
        https://leetcode.cn/problems/check-if-a-string-can-break-another-string
        """

        '''
        sort and compare?
        '''
        l1 = list(s1)
        l2= list(s2)
        l1.sort()
        l2.sort()

        largerInd = True
        smallerInd = True
        i = 0
        while i < len(l1):
            if l1[i] > l2[i]:
                smallerInd = False
                i+=1
            elif l1[i] < l2[i]:
                largerInd = False
                i+=1
            else:
                i+=1
        return largerInd or smallerInd
        # cost 10 mins
        # pass - 8.33/39.58
        # optimization - return all(a1<=a2 for a1,a2 in zip(l1,l2)) or all(a1>=a2 for a1,a2 in zip(l1,l2))
